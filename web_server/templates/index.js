$(document).ready(function() {
  var url = '{{HOST}}';
  var port = '{{PORT}}';
  var socket = io.connect(url + ':' + port);
  var intObj = null;
  
  socket.on('disconnect', function () {
    if (intObj !== null) {
      clearInterval(intObj)
      intObj = null
    }
    alert('Server Disconnected!')
  })
  socket.on('connect', function () {
    socket.emit('connect_response', {data: 'connected!'})
    intObj = setInterval(checkUpdate.bind(null, socket), 1000)
  })
  socket.on('temp_response', function (data) {
    updateRecord(data)
  })
  plotRecord()
});


function checkUpdate (socket) {
  socket.emit('check_temp', {})
}


function updateRecord (data) {
  console.log(data)
  $('#log').text(JSON.stringify(data))
  tar = $('#record_plot')[0]
  // see https://plotly.com/javascript/plotlyjs-function-reference/#plotlyprependtraces
  // prepend multiple traces up to a maximum of 10 points per trace
  // Plotly.prependTraces(tar, {y: [[rand()], [rand()]]}, [0, 1], 10)
}

function plotRecord () {
  console.log(moment().format('YYYY-MM-DD hh:mm:ss'))
  tar = $('#record_plot')[0]
  Plotly.plot(
    tar,
    [{
        x: [1, 2, 3, 4, 5],
        y: [1, 2, 4, 8, 16]
      },
      {
        x: [1, 2, 3, 4, 5],
        y: [1, 5, 6, 7, 19]
      },
      {
        x: [1, 2, 3, 4, 5],
        y: [3, 1, 2, 5, 10]
      }
    ],
    { margin: { t: 0 } },
    { showSendToCloud: true }
  );
}
