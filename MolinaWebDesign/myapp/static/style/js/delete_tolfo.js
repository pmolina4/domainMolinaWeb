        var form = document.getElementById("deletForm");

        // Espera a que se envíe el formulario
        form.addEventListener("submit", function (event) {
            event.preventDefault(); // Evita que el formulario se envíe de inmediato
            Swal.fire({
                title: 'CORRECTO!',
                text: 'Toldo Eliminado!!',
                icon: 'success',
                showConfirmButton: false,
                timer: 3000
            }).then(function () {
                form.submit(); // Envía el formulario
            });
        });

