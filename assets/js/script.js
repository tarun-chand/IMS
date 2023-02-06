$(document).ready(function(){
    $('.search_select_box select').selectpicker();
})

$(".checkbox-input").click(function () {
    var backgroundColor = $(this).is(":checked") ? "beige;" : "";
    $(this)
      .closest("tr")
      .attr("style", "background-color: " + backgroundColor + "");
  });
  $("#checkAll").click(function () {
    $("input:checkbox").not(this).prop("checked", this.checked);
    var backgroundColor = $("input:checkbox").is(":checked")
      ? "beige;"
      : "";
    $("input:checkbox")
      .closest("tr")
      .attr("style", "background-color: " + backgroundColor + "");
  });