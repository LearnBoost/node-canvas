{
    'includes': ['common.gyp', 'locations.gyp'],
    'conditions':
    [
        ['OS!="win"', {
            'variables':
            {
                'cairo_src%': "<(cairo_root)cairo/"
            },
        }]
    ],
    'targets':
    [{
        'target_name': 'cairo',
        'type': 'static_library',
        'include_dirs':
        [
            'custom-include/cairo',
            '<(cairo_root)',
            '<(cairo_src)',
            '<(fontconfig_root)',
            '<(freetype_root)include',
            '<(libpng_root)',
            'custom-include/png',
            '<(pixman_root)',
            '<(pixman_root)pixman',
            '<(zlib_root)',
        ],
        'dependencies':
        [
            'pixman.gyp:pixman',
            'freetype.gyp:freetype',
        ],
        'defines': ['HAVE_CONFIG_H'],

        # 'cflags!': [ '-O2' ],
        # 'cflags+': [ '-O3' ],
        # 'cflags_cc!': [ '-O2' ],
        # 'cflags_cc+': [ '-O3' ],
        # 'cflags_c!': [ '-O2' ],
        # 'cflags_c+': [ '-O3' ],
        'sources':
        [
            "<(cairo_src)cairo-analysis-surface.c",
            "<(cairo_src)cairo-arc.c",
            "<(cairo_src)cairo-array.c",
            "<(cairo_src)cairo-atomic.c",
            "<(cairo_src)cairo-base64-stream.c",
            "<(cairo_src)cairo-base85-stream.c",
            "<(cairo_src)cairo-bentley-ottmann.c",
            "<(cairo_src)cairo-bentley-ottmann-rectangular.c",
            "<(cairo_src)cairo-bentley-ottmann-rectilinear.c",
            "<(cairo_src)cairo-botor-scan-converter.c",
            "<(cairo_src)cairo-boxes.c",
            "<(cairo_src)cairo-boxes-intersect.c",
            "<(cairo_src)cairo.c",
            "<(cairo_src)cairo-cache.c",
            "<(cairo_src)cairo-cff-subset.c",
            "<(cairo_src)cairo-clip-boxes.c",
            "<(cairo_src)cairo-clip.c",
            "<(cairo_src)cairo-clip-polygon.c",
            "<(cairo_src)cairo-clip-region.c",
            "<(cairo_src)cairo-clip-surface.c",
            "<(cairo_src)cairo-clip-tor-scan-converter.c",
            # "<(cairo_src)cairo-cogl-context.c",
            # "<(cairo_src)cairo-cogl-gradient.c",
            # "<(cairo_src)cairo-cogl-surface.c",
            # "<(cairo_src)cairo-cogl-utils.c",
            "<(cairo_src)cairo-color.c",
            "<(cairo_src)cairo-composite-rectangles.c",
            "<(cairo_src)cairo-compositor.c",
            "<(cairo_src)cairo-contour.c",
            "<(cairo_src)cairo-damage.c",
            "<(cairo_src)cairo-debug.c",
            "<(cairo_src)cairo-default-context.c",
            "<(cairo_src)cairo-deflate-stream.c",
            "<(cairo_src)cairo-device.c",
            # "<(cairo_src)cairo-directfb-surface.c",
            # "<(cairo_src)cairo-egl-context.c",
            "<(cairo_src)cairo-error.c",
            "<(cairo_src)cairo-fallback-compositor.c",
            "<(cairo_src)cairo-fixed.c",
            "<(cairo_src)cairo-font-face.c",
            "<(cairo_src)cairo-font-face-twin.c",
            "<(cairo_src)cairo-font-face-twin-data.c",
            "<(cairo_src)cairo-font-options.c",
            "<(cairo_src)cairo-freed-pool.c",
            "<(cairo_src)cairo-freelist.c",
            "<(cairo_src)cairo-ft-font.c",
            # "<(cairo_src)cairo-gl-composite.c",
            # "<(cairo_src)cairo-gl-device.c",
            # "<(cairo_src)cairo-gl-dispatch.c",
            # "<(cairo_src)cairo-gl-glyphs.c",
            # "<(cairo_src)cairo-gl-gradient.c",
            # "<(cairo_src)cairo-gl-info.c",
            # "<(cairo_src)cairo-gl-msaa-compositor.c",
            # "<(cairo_src)cairo-gl-operand.c",
            # "<(cairo_src)cairo-gl-shaders.c",
            # "<(cairo_src)cairo-gl-source.c",
            # "<(cairo_src)cairo-gl-spans-compositor.c",
            # "<(cairo_src)cairo-gl-surface.c",
            # "<(cairo_src)cairo-gl-traps-compositor.c",
            # "<(cairo_src)cairo-glx-context.c",
            "<(cairo_src)cairo-gstate.c",
            "<(cairo_src)cairo-hash.c",
            "<(cairo_src)cairo-hull.c",
            "<(cairo_src)cairo-image-compositor.c",
            "<(cairo_src)cairo-image-info.c",
            "<(cairo_src)cairo-image-source.c",
            "<(cairo_src)cairo-image-surface.c",
            "<(cairo_src)cairo-lzw.c",
            "<(cairo_src)cairo-mask-compositor.c",
            "<(cairo_src)cairo-matrix.c",
            "<(cairo_src)cairo-mempool.c",
            "<(cairo_src)cairo-mesh-pattern-rasterizer.c",
            "<(cairo_src)cairo-misc.c",
            "<(cairo_src)cairo-mono-scan-converter.c",
            "<(cairo_src)cairo-mutex.c",
            "<(cairo_src)cairo-no-compositor.c",
            "<(cairo_src)cairo-observer.c",
            # "<(cairo_src)cairo-os2-surface.c",
            "<(cairo_src)cairo-output-stream.c",
            "<(cairo_src)cairo-paginated-surface.c",
            "<(cairo_src)cairo-path-bounds.c",
            "<(cairo_src)cairo-path.c",
            "<(cairo_src)cairo-path-fill.c",
            "<(cairo_src)cairo-path-fixed.c",
            "<(cairo_src)cairo-path-in-fill.c",
            "<(cairo_src)cairo-path-stroke-boxes.c",
            "<(cairo_src)cairo-path-stroke.c",
            "<(cairo_src)cairo-path-stroke-polygon.c",
            "<(cairo_src)cairo-path-stroke-traps.c",
            "<(cairo_src)cairo-path-stroke-tristrip.c",
            "<(cairo_src)cairo-pattern.c",
            "<(cairo_src)cairo-pdf-operators.c",
            "<(cairo_src)cairo-pdf-shading.c",
            "<(cairo_src)cairo-pdf-surface.c",
            "<(cairo_src)cairo-pen.c",
            "<(cairo_src)cairo-png.c",
            "<(cairo_src)cairo-polygon.c",
            "<(cairo_src)cairo-polygon-intersect.c",
            "<(cairo_src)cairo-polygon-reduce.c",
            "<(cairo_src)cairo-ps-surface.c",
            "<(cairo_src)cairo-raster-source-pattern.c",
            "<(cairo_src)cairo-recording-surface.c",
            "<(cairo_src)cairo-rectangle.c",
            "<(cairo_src)cairo-rectangular-scan-converter.c",
            "<(cairo_src)cairo-region.c",
            "<(cairo_src)cairo-rtree.c",
            "<(cairo_src)cairo-scaled-font.c",
            "<(cairo_src)cairo-scaled-font-subsets.c",
            # "<(cairo_src)cairo-script-surface.c",
            "<(cairo_src)cairo-shape-mask-compositor.c",
            "<(cairo_src)cairo-slope.c",
            "<(cairo_src)cairo-spans.c",
            "<(cairo_src)cairo-spans-compositor.c",
            "<(cairo_src)cairo-spline.c",
            "<(cairo_src)cairo-stroke-dash.c",
            "<(cairo_src)cairo-stroke-style.c",
            "<(cairo_src)cairo-surface.c",
            "<(cairo_src)cairo-surface-clipper.c",
            "<(cairo_src)cairo-surface-fallback.c",
            "<(cairo_src)cairo-surface-observer.c",
            "<(cairo_src)cairo-surface-offset.c",
            "<(cairo_src)cairo-surface-snapshot.c",
            "<(cairo_src)cairo-surface-subsurface.c",
            "<(cairo_src)cairo-surface-wrapper.c",
            "<(cairo_src)cairo-svg-surface.c",
            # "<(cairo_src)cairo-tee-surface.c",
            "<(cairo_src)cairo-time.c",
            "<(cairo_src)cairo-tor22-scan-converter.c",
            "<(cairo_src)cairo-tor-scan-converter.c",
            "<(cairo_src)cairo-toy-font-face.c",
            "<(cairo_src)cairo-traps.c",
            "<(cairo_src)cairo-traps-compositor.c",
            "<(cairo_src)cairo-tristrip.c",
            "<(cairo_src)cairo-truetype-subset.c",
            "<(cairo_src)cairo-type1-fallback.c",
            "<(cairo_src)cairo-type1-glyph-names.c",
            "<(cairo_src)cairo-type1-subset.c",
            "<(cairo_src)cairo-type3-glyph-surface.c",
            "<(cairo_src)cairo-unicode.c",
            "<(cairo_src)cairo-user-font.c",
            "<(cairo_src)cairo-version.c",
            # "<(cairo_src)cairo-vg-surface.c",
            # "<(cairo_src)cairo-wgl-context.c",
            "<(cairo_src)cairo-wideint.c",
            # "<(cairo_src)cairo-xcb-connection.c",
            # "<(cairo_src)cairo-xcb-connection-core.c",
            # "<(cairo_src)cairo-xcb-connection-render.c",
            # "<(cairo_src)cairo-xcb-connection-shm.c",
            # "<(cairo_src)cairo-xcb-screen.c",
            # "<(cairo_src)cairo-xcb-shm.c",
            # "<(cairo_src)cairo-xcb-surface.c",
            # "<(cairo_src)cairo-xcb-surface-core.c",
            # "<(cairo_src)cairo-xcb-surface-render.c",
            # "<(cairo_src)cairo-xml-surface.c",
            # "<(cairo_src)check-has-hidden-symbols.c",
            "<(cairo_src)check-link.c",
            # "<(cairo_src)drm/cairo-drm-bo.c",
            # "<(cairo_src)drm/cairo-drm.c",
            # "<(cairo_src)drm/cairo-drm-gallium-surface.c",
            # "<(cairo_src)drm/cairo-drm-i915-glyphs.c",
            # "<(cairo_src)drm/cairo-drm-i915-shader.c",
            # "<(cairo_src)drm/cairo-drm-i915-spans.c",
            # "<(cairo_src)drm/cairo-drm-i915-surface.c",
            # "<(cairo_src)drm/cairo-drm-i965-glyphs.c",
            # "<(cairo_src)drm/cairo-drm-i965-shader.c",
            # "<(cairo_src)drm/cairo-drm-i965-spans.c",
            # "<(cairo_src)drm/cairo-drm-i965-surface.c",
            # "<(cairo_src)drm/cairo-drm-intel-brw-eu.c",
            # "<(cairo_src)drm/cairo-drm-intel-brw-eu-emit.c",
            # "<(cairo_src)drm/cairo-drm-intel-brw-eu-util.c",
            # "<(cairo_src)drm/cairo-drm-intel.c",
            # "<(cairo_src)drm/cairo-drm-intel-debug.c",
            # "<(cairo_src)drm/cairo-drm-intel-surface.c",
            # "<(cairo_src)drm/cairo-drm-radeon.c",
            # "<(cairo_src)drm/cairo-drm-radeon-surface.c",
            # "<(cairo_src)drm/cairo-drm-surface.c",
            "<(cairo_src)test-base-compositor-surface.c",
            "<(cairo_src)test-compositor-surface.c",
            "<(cairo_src)test-null-compositor-surface.c",
            "<(cairo_src)test-paginated-surface.c",
        ]
    }]
}
