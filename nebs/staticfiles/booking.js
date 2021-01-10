function createGrid(col, row){
    days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"];
    d_cnt = 0;
    times = ["6AM","7AM","8AM","9AM","10AM","11AM","12AM","1PM","2PM",
    "3PM","4PM","5PM","6PM","7PM","8PM","9PM","10PM","11PM"];
    timesp = ["6:00AM","7:00AM","8:00AM","9:00AM","10:00AM","11:00AM","12:00AM","1:00PM","2:00PM",
    "3:00PM","4:00PM","5:00PM","6:00PM","7:00PM","8:00PM","9:00PM","10:00PM","11:00PM"];
    t_cnt = 0;
    document.getElementById('container-booking').innerHTML = "";
    for(let i = 0; i < col; i++){
       let col = document.createElement('div');
       col.className = "col"; 
       for(let j = 0; j < row; j++){
           let box = document.createElement('div');
           if(i == 0 && j == 0){
            box.className = "box useless";
           }else if(j == 0 && i > 0){
               box.className = "box day-name";
               box.innerHTML = days[d_cnt];
               d_cnt++;
           }else if(i == 0){
               box.className = "box time-name";
               box.innerHTML = timesp[t_cnt];
               t_cnt++;
           }else{
               str = days[i-1] + "-" + times[j-1];
               box.className = "box time-slot " + str;
           }
           
           col.appendChild(box);
       }
       document.getElementById('container-booking').appendChild(col);
    }
}

createGrid(8, 19);

bookingButton = document.querySelector('.send-booking-request');
closeForm = document.querySelector('.close-container');
bookingForm = document.querySelector('.container');

bookingButton.addEventListener('click', ()=>{
    bookingForm.style.display = "block";
});

closeForm.addEventListener('click', ()=>{
    bookingForm.style.display = "none";
});


