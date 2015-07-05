#include "ImageBackend.h"

ImageBackend::ImageBackend(int width, int height) {
	this->name = "image";

	this->width = width;
	this->height = height;
}

cairo_surface_t *ImageBackend::createSurface() {
	this->surface = cairo_image_surface_create(CAIRO_FORMAT_ARGB32, this->width, this->height);
	return this->surface;
}

cairo_surface_t *ImageBackend::recreateSurface() {
	if (this->surface != NULL) {
		cairo_surface_destroy(this->surface);
	}
	this->surface = cairo_image_surface_create(CAIRO_FORMAT_ARGB32, width, height);
	return this->surface;
}

void ImageBackend::destroySurface() {
	if (this->surface != NULL) {
		cairo_surface_destroy(this->surface);
	}
}

Persistent<FunctionTemplate> ImageBackend::constructor;

void ImageBackend::Initialize(Handle<Object> target) {
	NanScope();
	Local<FunctionTemplate> ctor = NanNew<FunctionTemplate>(ImageBackend::New);
	NanAssignPersistent(ImageBackend::constructor, ctor);
	ctor->InstanceTemplate()->SetInternalFieldCount(1);
	ctor->SetClassName(NanNew("ImageBackend"));
	target->Set(NanNew("ImageBackend"), ctor->GetFunction());
}

NAN_METHOD(ImageBackend::New) {
	int width = 0;
	int height = 0;
	if (args[0]->IsNumber()) width = args[0]->Uint32Value();
	if (args[1]->IsNumber()) height = args[1]->Uint32Value();

	ImageBackend *backend = new ImageBackend(width, height);
	backend->Wrap(args.This());
	NanReturnValue(args.This());
}
