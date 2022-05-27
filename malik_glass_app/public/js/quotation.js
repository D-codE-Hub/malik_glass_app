
frappe.ui.form.on("Quotation Item", {
	
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
})


let set_datas = function(frm, cdt, cdn) {
	var d = frappe.model.get_doc(cdt, cdn);

	frappe.model.set_value(d.doctype, d.name, "qty",1);

	frappe.model.set_value(d.doctype, d.name, "per_sqm",  d.height*d.width);
	frappe.model.set_value(d.doctype, d.name, "total_sqm",  d.per_sqm*d.quantity_of_glass );
	frappe.model.set_value(d.doctype, d.name, "qty",  d.total_sqm);

	frappe.model.set_value(d.doctype, d.name, "running_meter",  ((d.side_h*d.height)+(d.side_w*d.width))*d.quantity_of_glass);
	frm.set_value("total_running_mtr", 0);
	for (let row of frm.doc.items) {
		frm.doc.total_running_mtr += flt(row.running_meter);
	}
	frm.refresh_field("total_running_mtr");
}