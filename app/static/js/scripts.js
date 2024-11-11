$(document).ready(function () {
    loadGoals();

    // Ziele laden und Tabelle anzeigen
    function loadGoals() {
        $.get("/goals", function (data) {
            $("#goals-table-body").empty();
            data.goals.forEach(goal => {
                $("#goals-table-body").append(`
                    <tr>
                        
                        <td>${goal.id}</td>
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

            // Bearbeiten-Klick-Event
            $(".edit-goal").click(function() {
                const goalId = $(this).data("id");
                $.get(`/goals/${goalId}`, function(data) {
                    const goal = data.goal;
                    $("#edit-goal-id").val(goal.id);
                    $("#edit-department").val(goal.department);
                    $("#edit-statement").val(goal.statement);
                    $("#edit-success-criteria").val(goal.success_criteria);
                    $("#edit-rating").val(goal.rating);
                    $("#edit-assessment").val(goal.assessment);
                    $("#editGoalModal").modal("show");
                });
            });
        });
    }

    // Formular-Submit für Bearbeiten
    $("#edit-goal-form").submit(function(event) {
        event.preventDefault();
        
        const goalId = $("#edit-goal-id").val();
        const updatedGoal = {
            department: $("#edit-department").val(),
            statement: $("#edit-statement").val(),
            success_criteria: $("#edit-success-criteria").val(),
            rating: $("#edit-rating").val(),
            assessment: $("#edit-assessment").val()
        };

        $.ajax({
            url: `/update_goal/${goalId}`,
            type: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify(updatedGoal),
            success: function(response) {
                alert(response.message);
                $("#editGoalModal").modal("hide");
                loadGoals();
            }
        });
    });

    // Klick-Event für das Hinzufügen-Button
$("#add-goal-btn").click(function() {
    $("#addGoalModal").modal("show");
});

// Absenden des Formulars für ein neues Ziel
$("#add-goal-form").submit(function(event) {
    event.preventDefault();
    
    const newGoalData = {
        department: $("#department").val(),
        statement: $("#statement").val(),
        success_criteria: $("#success_criteria").val(),
        rating: $("#rating").val(),
        assessment: $("#assessment").val()
    };
    
    $.ajax({
        type: "POST",
        url: "/add_goal",
        contentType: "application/json",
        data: JSON.stringify(newGoalData),
        success: function(response) {
            alert(response.message);
            $("#addGoalModal").modal("hide");
            // Seite aktualisieren oder neue Ziele in die Liste hinzufügen
            location.reload();
        },
        error: function() {
            alert("Fehler beim Hinzufügen des Ziels");
        }
    });
});


    
});
