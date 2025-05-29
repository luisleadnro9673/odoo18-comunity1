/** @odoo-module */

import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";

patch(PosOrder.prototype, {
    set_partner(partner) {
        super.set_partner(partner);
        if (this.config.sh_is_default_invoice){
            if(!partner){
                this.set_to_invoice(false)
            }else{
                if (this.config.sh_pos_default_invoice == "customer_wise_invoice"){
                    if (partner && partner.sh_enable_auto_invoice){
                        this.set_to_invoice(true)
                    }else{
                        
                        this.set_to_invoice(false)
                    }
                }
                else {
                    if (partner){
                        this.set_to_invoice(true)
                    }
                }
            }
        }
    },
});
