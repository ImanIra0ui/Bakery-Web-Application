function createGrid(col, row){
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    d_cnt = 0;
    times = ["6:00AM","7:00AM","8:00AM","9:00AM","10:00AM","11:00AM","12:00AM","1:00PM","2:00PM",
    "3:00PM","4:00PM","5:00PM","6:00PM","7:00PM","8:00PM","9:00PM","10:00PM","11:00PM","00:00PM",];
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
               box.innerHTML = times[t_cnt];
               t_cnt++;
           }else{
               box.className = "box time-slot";
           }
           
           col.appendChild(box);
       }
       document.getElementById('container-booking').appendChild(col);
    }
}

createGrid(8, 19);