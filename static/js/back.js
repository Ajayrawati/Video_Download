document.addEventListener("DOMContentLoaded", function () {
   
    
    if (formats && formats.length > 0) {
      const downloadSection = document.querySelector('.formats-list'); 
      
      formats.forEach(function(format) {
        const listItem = document.createElement('li');
        
        const button = document.createElement('a');
        button.href = format.url;  
        button.textContent = 'Download ' + (format.extension || 'Video');  
        button.classList.add('download-button');  
        
        listItem.appendChild(button);
        
        downloadSection.appendChild(listItem);
      });
    } else {
      console.log('No formats available or formats are empty.');
    }
});

