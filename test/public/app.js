window.addEventListener('load', runTests)

function create (type, attrs, children) {
  const element = Object.assign(document.createElement(type), attrs)

  if (children) {
    children.forEach(function (child) { element.appendChild(child) })
  }

  return element
}

function pdfLink (name) {
  return create('a', {
    href: '/pdf?name=' + encodeURIComponent(name),
    target: '_blank',
    textContent: 'PDF'
  })
}

function localRendering (name) {
  var canvas = create('canvas', { width: 200, height: 200, title: name })

  var ctx = canvas.getContext('2d', {alpha: true})
  var initialFillStyle = ctx.fillStyle
  ctx.fillStyle = 'white'
  ctx.fillRect(0, 0, 200, 200)
  ctx.fillStyle = initialFillStyle
  window.tests[name](ctx, function () {})

  return canvas
}

function getDifference(canvas, image, outputCanvas) {
  var imgCanvas = create('canvas', { width: 200, height: 200, title: name });
  var ctx = imgCanvas.getContext('2d', {alpha: true});
  var output = ctx.getImageData(0, 0, 200, 200);
  ctx.drawImage(image, 0, 0, 200, 200);
  var imageDataCanvas = ctx.getImageData(0, 0, 200, 200).data;
  var imageDataGolden = canvas.getContext('2d', {alpha: true}).getImageData(0, 0, 200, 200).data;
  pixelmatch(imageDataCanvas, imageDataGolden, output.data, 200, 200, {
    includeAA: false,
    threshold: 0.15
  });
  outputCanvas.getContext('2d', {alpha: true}).putImageData(output, 0, 0);
  return outputCanvas;
}

function clearTests () {
  var table = document.getElementById('tests')
  if (table) document.body.removeChild(table)
}

function runTests () {
  clearTests()

  var testNames = Object.keys(window.tests)

  var table = create('table', { id: 'tests' }, [
    create('thead', {}, [
      create('th', { textContent: 'node-canvas' }),
      create('th', { textContent: 'browser canvas' }),
      create('th', { textContent: 'visual diffs' }),
      create('th', { textContent: '' })
    ]),
    create('tbody', {}, testNames.map(function (name) {
      var canvas = localRendering(name);
      var img = create('img', { src: '/render?name=' + encodeURIComponent(name) });
      var canvasOuput = create('canvas', { width: 200, height: 200, title: name });
      img.onload = function() {
        getDifference(canvas, img, canvasOuput);
      }
      return create('tr', {}, [
        create('td', {}, [img]),
        create('td', {}, [canvas]),
        create('td', {}, [canvasOuput]),
        create('td', {}, [create('h3', { textContent: name }), pdfLink(name)])
      ])
    }))
  ])

  document.body.appendChild(table)
}
