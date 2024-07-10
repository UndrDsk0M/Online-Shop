        // Select all elements with the class 'addcart'
        document.querySelectorAll('.addcart').forEach(button => {
          button.addEventListener('click', (event) => {
              const item = event.target.getAttribute('data-item');
              
              // Fetch data from the server
              fetch('/api/add-to-cart/', {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json',
                      // 'X-CSRFToken': getCookie('csrftoken') // Include CSRF token if necessary
                  },
                  body: JSON.stringify({ item: item })
              })
              .then(response => response.json())
              .then(data => {
                  console.log(data);
                  document.getElementById('dataContainer').innerText = JSON.stringify(data);
              })
              .catch(error => console.error('Error fetching data:', error));
          });
      });

      // // Function to get CSRF token from cookies
      // function getCookie(name) {
      //     let cookieValue = null;
      //     if (document.cookie && document.cookie !== '') {
      //         const cookies = document.cookie.split(';');
      //         for (let i = 0; i < cookies.length; i++) {
      //             const cookie = cookies[i].trim();
      //             // Does this cookie string begin with the name we want?
      //             if (cookie.substring(0, name.length + 1) === (name + '=')) {
      //                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
      //                 break;
      //             }
      //         }
      //     }
      //     return cookieValue;
      // }