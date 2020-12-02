document.addEventListener('DOMContentLoaded', () => {
  // Flash Message Box Delete Functionality
    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
      var $notification = $delete.parentNode;
  
      $delete.addEventListener('click', () => {
        $notification.parentNode.removeChild($notification);
      });
    });
//NavBar Mobile Menu
      // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
      el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });
  }
  });
  
// Delete Confirmation Dialog Box
  function confirmation() {
   
    if (confirm('Are you sure you want to Delete this Item?')) {
        // return "Yes" Delete
        return document.getElementById("deleteConfirm").value = "Yes";
      } else {
         // return "No" Do not Delete
        return document.getElementById("deleteConfirm").value = "No";
        
      };
  }
