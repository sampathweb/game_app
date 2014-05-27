$(function() {
  var app_toe = {
    game_choices: ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2", "2,0", "2,1", "2,2"],
    winning_combos: [["0,0", "0,1", "0,2"],
                      ["1,0", "1,1", "1,2"],
                      ["2,0", "2,1", "2,2"],
                      ["0,0", "1,0", "2,0"],
                      ["0,1", "1,1", "2,1"],
                      ["0,2", "1,2", "2,2"],
                      ["0,0", "1,1", "2,2"],
                      ["0,2", "1,1", "2,0"]],
    player_a: [],
    player_b: [],
    game_result: '',
    is_winner: function(player_a) {
      var count;
      for (var i=0; i < app_toe.winning_combos.length; i++) {
        var win_set = app_toe.winning_combos[i];
        count = 0;
        for (var j=0; j < win_set.length; j++) {
          var item = win_set[j];
          if (player_a.indexOf(item) !== -1) {
            count += 1;
          }
        };
        if (count === 3) {
          return true;
        }
      };

      return false;
    }
  };
// On Play Gain, reset the game
  $("ul.row button").on("click", function(event) {
    event.preventDefault();
    var button = $(this);
    var sel_item = button.val();
    app_toe.player_a.push(sel_item);
    app_toe.game_choices.splice(app_toe.game_choices.indexOf(sel_item), 1);
    var content = button.find(".content");
    if (content) {
      // set the game matrix
      content.text($('#player-piece').val());
      button.prop("disabled", true);
      button.off("click");
      // Check game over
      if (app_toe.is_winner(app_toe.player_a)) {
        $('.result').text('You Won!');
      }
      // Computer to Pick a slot
      // sel_item = app_toe.computer_slot();
      // if (sel_item) {
      //   app_toe.player_b.push(sel_item);
      //   app_toe.game_choices.splice(app_toe.game_choices.indexOf(sel_item), 1);
      //   button = $('button[value="'+sel_item+'"]');
      //   if (button) {
      //     content = button.find(".content");
      //     content.text('O');
      //     button.prop("disabled", true);
      //     // button.off("click");
      //   }
      }
      if (app_toe.is_winner(app_toe.player_b)) {
        $('.result').text('You Lost.  Better luck next times');
      }
      // If there are no more slots, end the game
      if (app_toe.game_choices.length === 0) {
        $('.result').text('Its a Draw. Play Again?');
      }
  });


    namespace = 'sockets'; // change to an empty string to use the global namespace

    // the socket.io documentation recommends sending an explicit package upon connection
    // this is specially important when using the global namespace
    var socket = io.connect(window.location.href + namespace);
    console.log(window.location.href + namespace);
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });

    // event handler for server sent data
    // the data is displayed in the "Received" section of the page
    socket.on('response', function(msg) {
        $('#log').append('<br>Received #' + msg.count + ': ' + msg.data);
    });

  $(".js-new-game").on("click", function(event) {
    event.preventDefault();
    // navigate to the new page and append a random number at the end of the url
    socket.emit('join', {room: ''});
  });

  $(".js-join-game").on("click", function(event) {
    event.preventDefault();
    // navigate to the new page and append a random number at the end of the url
    console.log($('#room-name').val());
    socket.emit('join', {room: $('#room-name').val()});
  });

  $("ul.row button").on("click", function(event) {
    event.preventDefault();
    var button = $(this);
    var sel_item = button.val();
    socket.emit('player-move', {room: $('#room_name').val(), data: sel_item});
  });

    socket.on('game-response', function(msg) {
        $('#log').append('<br>Received Game Response #' + msg.count + ': ' + msg.data);
    });

    // handlers for the different forms in the page
    // these send data to the server in a variety of ways
    $('form#emit').submit(function(event) {
        socket.emit('my-event', {data: $('#emit_data').val()});
        return false;
    });
    $('form#broadcast').submit(function(event) {
        socket.emit('broadcast-event', {data: $('#broadcast_data').val()});
        return false;
    });
    $('form#join').submit(function(event) {
        socket.emit('join', {room: $('#join_room').val()});
        return false;
    });
    $('form#leave').submit(function(event) {
        socket.emit('leave', {room: $('#leave_room').val()});
        return false;
    });
    $('form#send_room').submit(function(event) {
        socket.emit('room-event', {room: $('#room_name').val(), data: $('#room_data').val()});
        return false;
    });
});