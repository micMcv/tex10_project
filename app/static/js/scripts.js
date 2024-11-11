// Laden aller Ziele
$(document).ready(function () {
    loadGoals();

    // Zielübersicht laden
    function loadGoals() {
        $.get("/goals", function (data) {
            $("#goals-table-body").empty();
            data.goals.forEach(goal => {
                $("#goals-table-body").append(`
                    <tr>
                        <td>${goal.department}</td>
                        <td>${goal.statement}</td>
                        <td>${goal.success_criteria}</td>
                        <td>${goal.rating}</td>
                        <td>${goal.last_modified}</td>
                        <td>
                            <button class="btn btn-info view-goal" data-id="${goal.id}">Ansehen</button>
                            <button class="btn btn-warning edit-goal" data-id="${goal.id}">Bearbeiten</button>
                        </td>
                    </tr>
                `);
            });
        });
    }

    // Beispiel-Handler zum Hinzufügen eines neuen Ziels
    $('#add-goal-btn').click(function() {
        let newGoal = {
            department: "Beispielabteilung",
            statement: "Beispielaussage",
            success_criteria: "Erfolgskriterium",
            rating: 5,
            assessment: "Zwischenerfolg"
        };

        $.post("/add_goal", JSON.stringify(newGoal), function (response) {
            alert(response.message);
            loadGoals();
        }, "json");
    });
});
