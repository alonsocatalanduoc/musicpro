  // Array para almacenar los productos en el carrito
  var carrito = [];
  
  // Función para agregar un producto al carrito
  function agregarAlCarrito(nombre, precio) {
    // Crear un objeto producto
    var producto = {
      nombre: nombre,
      precio: precio
    };

    // Agregar el producto al carrito
    carrito.push(producto);

    // Actualizar la interfaz de usuario
    actualizarInterfazUsuario();
  }

  // Función para eliminar un producto del carrito
  function eliminarDelCarrito(index) {
    // Eliminar el producto del carrito en la posición indicada por el índice
    carrito.splice(index, 1);

    // Actualizar la interfaz de usuario
    actualizarInterfazUsuario();
  }

  // Función para actualizar la interfaz de usuario del carrito
  function actualizarInterfazUsuario() {
    var carritoLista = document.getElementById("carrito-lista");
    var totalElement = document.getElementById("total");
    
    // Limpiar la lista del carrito
    carritoLista.innerHTML = "";

    // Variable para calcular el total
    var total = 0;

    // Recorrer el carrito y actualizar la lista
    carrito.forEach(function(producto, index) {
      var listItem = document.createElement("li");
      listItem.className = "list-group-item";
      listItem.innerHTML = `<span>${producto.nombre}</span> - $${producto.precio.toFixed(2)} 
                            <button class="btn btn-danger btn-sm float-end" onclick="eliminarDelCarrito(${index})">Eliminar</button>`;
      carritoLista.appendChild(listItem);

      // Actualizar el total
      total += producto.precio;
    });

    // Actualizar el total en la interfaz de usuario
    totalElement.textContent = total.toFixed(2);
  }