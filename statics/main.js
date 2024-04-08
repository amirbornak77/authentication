document.getElementById('registerForm').addEventListener('submit', function(event){
    event.preventDefault();
    const formData = {
      firstName: document.getElementById('firstName').value,
      lastName: document.getElementById('lastName').value,
      phone: document.getElementById('phone').value,
      email: document.getElementById('email').value
    };
    console.log(formData);
    // Here you can add what to do with the formData, e.g., send it to a server
  });