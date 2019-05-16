function change() {

    var cc_i = document.getElementById("cc_F");
    var ex_i = document.getElementById("ex_F");
    var cvv_i = document.getElementById("cvv_F");

    var sn_i = document.getElementById("sn_F");
    var hn_i = document.getElementById("hn_F");
    var c_i = document.getElementById("c_F");
    var cn_i = document.getElementById("cn_F");
    var pc_i = document.getElementById("pc_F");
    var sc_i = document.getElementById("sc_F");


    document.getElementById("CCN").innerHTML = cc_i.value;
    document.getElementById("EX").innerHTML = ex_i.value;
    document.getElementById("CVV").innerHTML = cvv_i.value;
    

    document.getElementById("SN").innerHTML = sn_i.value;
    document.getElementById("HN").innerHTML = hn_i.value;
    document.getElementById("Ct").innerHTML = c_i.value;
    document.getElementById("Cn").innerHTML = cn_i.value;
    document.getElementById("PC").innerHTML = pc_i.value;
    document.getElementById("SC").innerHTML = sc_i.value;


}