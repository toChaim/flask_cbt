$(document).ready(function() {
	var user_id = $("#user_id").val();
	var csrf_token = $("#csrf_token").val();
	var $board = $("#board");
	var $prompt = $("#prompt h2");
	var $btn2 = $("#btn2");
	var $btn3 = $("#btn3");
	var allArr = [];
	var goodMessages = [
		"Yeah!!!",
		"Right On",
		"You Win!",
		"Shazam",
		"Nice work.",
		"Pow"
	];
	var badNews = ["Oops", "uh oh", "ouch!"];

	$board.on("click", "button", function(e) {
		if ($(e.target).data("win")) {
			$board.after(
				$("<p>", {
					id: "flash",
					text: goodMessages[Math.floor(Math.random() * goodMessages.length)],
					class: "flash"
				})
			);
		}
		display(matchConstruct());
	});

	var url = `/users/${user_id}/matches`;
	var promis = $.get(url).then(function(data) {
		allArr = data;
		display(matchConstruct());
	});

	function display(match_obj) {
		// job to know about the board
		$prompt.text(match_obj.prompt.title);
		$btn2.text(match_obj.leftResponse.title);
		$btn2.data(
			"win",
			match_obj.leftResponse.affirmation === match_obj.prompt.affirmation
		);
		if (match_obj.rightResponse) {
			$btn3.text(match_obj.rightResponse.title);
			$btn3.data(
				"win",
				match_obj.rightResponse.affirmation === match_obj.prompt.affirmation
			);
		} else {
			$btn3.text("");
			$btn3.data("win", false);
		}
	}

	function matchConstruct(arr = allArr) {
		// pick one match from all_possible_matches_obj
		var prompt = arr[Math.floor(Math.random() * arr.length)];
		var leftResponse =
			prompt.responses[Math.floor(Math.random() * prompt.responses.length)];
		var otherPossibleResponses = prompt.responses.filter(
			v => leftResponse.affirmation !== v.affirmation
		);
		var rightResponse =
			otherPossibleResponses[
				Math.floor(Math.random() * otherPossibleResponses.length)
			];
		return { prompt, leftResponse, rightResponse };
	}

	function scoreMatch(match_obj, btn_click) {
		// score and eventualy store match
	}
});
