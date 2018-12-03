#ifndef __BACKEND_H__
#define __BACKEND_H__

#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <exception>

#include <v8.h>
#include <nan.h>
#include <cairo.h>

#include "../dll_visibility.h"

class Canvas;

using namespace std;

using Nan::Callback;


typedef map<long, Callback*> map_callbacks;


class Backend : public Nan::ObjectWrap
{
  private:
    const string name;
    const char* error = NULL;

    uv_thread_t vSyncThread;
    long requestID;

    void dispatchWaitVSync();

  protected:
    int width;
    int height;
    cairo_surface_t* surface;
    Canvas* canvas;

    Backend(string name, int width, int height);
    static void init(const Nan::FunctionCallbackInfo<v8::Value> &info);
    static Backend *construct(int width, int height){ return nullptr; }

  public:
    bool listenOnPaint;
    bool waitingVSync;
    map_callbacks* raf_callbacks;

    virtual ~Backend();

    void setCanvas(Canvas* canvas);

    virtual cairo_surface_t* createSurface() = 0;
    virtual cairo_surface_t* recreateSurface();

    DLL_PUBLIC cairo_surface_t* getSurface();
    void             destroySurface();

    DLL_PUBLIC string getName();

    DLL_PUBLIC int getWidth();
    virtual void setWidth(int width);

    DLL_PUBLIC int getHeight();
    virtual void setHeight(int height);

    // Overridden by ImageBackend. SVG and PDF thus always return INVALID.
    virtual cairo_format_t getFormat() {
      return CAIRO_FORMAT_INVALID;
    }

    bool isSurfaceValid();
    inline const char* getError(){ return error; }

    void onPaint();

    virtual void waitVSync(){};
    virtual void swapBuffers(){};
    void executeCallbacks();

    NAN_METHOD(requestAnimationFrame);
    NAN_METHOD(cancelAnimationFrame);
};


class BackendOperationNotAvailable: public exception
{
  private:
    Backend* backend;
    string operation_name;

  public:
    BackendOperationNotAvailable(Backend* backend, string operation_name);
    ~BackendOperationNotAvailable() throw();

    const char* what() const throw();
};

#endif
