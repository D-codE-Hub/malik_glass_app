
frappe.ui.form.on("Sales Invoice Item", {
	
	height: function(frm, cdt, cdn) {
		set_datas(frm, cdt, cdn);
	},

	width: function(frm, cdt, cdn) {
		set_datas(frm, cdt, cdn);
	},

	side_h: function(frm, cdt, cdn) {
		set_datas(frm, cdt, cdn);
	},

	side_w: function(frm, cdt, cdn) {
		set_datas(frm, cdt, cdn);
	},

	quantity_of_glass: function(frm, cdt, cdn) {
		set_datas(frm, cdt, cdn);
	},

	unit: function(frm, cdt, cdn) {
		set_datas(frm, cdt, cdn);
	},
})


let set_datas = function(frm, cdt, cdn) {
	var d = frappe.model.get_doc(cdt, cdn);
	var height = d.height;
	var width = d.width;
	if (d.unit=="CM"){
		
		var height = d.height/100;
		var width = d.width/100;
	}
	var per_sqm =  height*width
	var running_meter = ((d.side_h*height)+(d.side_w*width))*d.quantity_of_glass
	if (per_sqm < 0.5){
		per_sqm = 0.5;
	}
	if (running_meter < 1){
		running_meter = 1;
	}
	// console.log(height*width)
	frappe.model.set_value(d.doctype, d.name, "qty",1);

	frappe.model.set_value(d.doctype, d.name, "per_sqm", per_sqm);
	frappe.model.set_value(d.doctype, d.name, "total_sqm",  d.per_sqm*d.quantity_of_glass );
	frappe.model.set_value(d.doctype, d.name, "qty",  d.total_sqm);

	frappe.model.set_value(d.doctype, d.name, "running_meter", running_meter);
	frm.set_value("total_running_mtr", 0);
	frm.set_value("total_sqm", 0);
	for (let row of frm.doc.items) {
		frm.doc.total_running_mtr += flt(row.running_meter);
		frm.doc.total_sqm += flt(row.total_sqm);
	}
	frm.refresh_field("total_running_mtr");
	frm.refresh_field("total_sqm");
}