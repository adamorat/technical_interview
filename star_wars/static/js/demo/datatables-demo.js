// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    "language": {
      "lengthMenu": "Mostrar _MENU_ elementos por página",
      "zeroRecords": "Nada encontrado - lo sentimos",
      "info": "Mostrando página _PAGE_ de _PAGES_",
      "infoEmpty": "Sin registros disponibles",
      "search": "Buscar",
      "paginate": {
        "next":       "Siguiente",
        "previous":   "Anterior"
      },
    }
  });
});
