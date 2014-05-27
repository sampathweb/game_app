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

    computer_slot: function() {
      // Play Harder
      var win_set, item, block_line, win_line, is_blocked, is_defended;
      for (var i=0; i < app_toe.winning_combos.length; i++) {
        win_set = app_toe.winning_combos[i];
        block_line = [];
        win_line = [];
        is_blocked = false;
        is_defended = false;
        for (var j=0; j < win_set.length; j++) {
          item = win_set[j];
          if (app_toe.player_a.indexOf(item) === -1) {
            block_line.push(item);
          }
          else {
            is_blocked = true;
          }
          if (app_toe.player_b.indexOf(item) === -1) {
            win_line.push(item);
          }
          else {
            is_defended = true;
          }
        };
        if (win_line.length === 1 && !is_blocked) {
          return win_line.pop();
        }
        if (block_line.length === 1 && !is_defended) {
          return block_line.pop();
        }
      }
      if (app_toe.game_choices.length > 0) {
        console.log('pop any item');
        return app_toe.game_choices[0];
      }
    },

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
