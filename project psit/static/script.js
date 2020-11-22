function sivamtime() {
    now = new Date();
    d = now.getDay();
    m = now.getMonth() + 1;
    y = now.getFullYear() + 543;
    hour = now.getHours();
    min = now.getMinutes();
    sec = now.getSeconds();
    days = new Array('อาทิตย์', 'จันทร์', 'อังคาร', 'พุธ', 'พฤหัสบดี', 'ศุกร์', 'เสาร์');
    months = new Array('มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม');


    if (min <= 9) { min = "0" + min; }
    if (sec <= 9) { sec = "0" + sec; }
    if (hour > 12) { hour = hour - 12; add = "pm"; }
    else { hour = hour; add = "am"; }
    if (hour == 12) { add = "pm"; }

    time = "วัน" + days[d] + " " + "เดือน" + months[m] + " " + y + "   " + "เวลา" + "  " + hour + ":" + min + ":" + sec + " " + add;;

    if (document.getElementById) { date.innerHTML = time; }
    else if (document.layers) {
        document.layers.date.document.write(time);
        document.layers.date.document.close();
    }

    setTimeout("sivamtime()", 1000);
}
window.onload = sivamtime;

//  https://www.thaicreate.com/php/forum/025326.html credit

