$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "type the correct answer -_-");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                subject: {
                    required: true,
                    minlength: 4
                },
                number: {
                    required: true,
                    minlength: 5
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true,
                    minlength: 20
                }
            },
            messages: {
                name: {
                    required: "Saisir vos nom",
                    minlength: "Votre nom doit etre au moins 2 characters"
                },
                subject: {
                    required: "Saisir le sujet",
                    minlength: "Au moins 4 characters"
                },
                number: {
                    required: "come on, you have a number, don't you?",
                    minlength: "your Number must consist of at least 5 characters"
                },
                email: {
                    required: "pas de mail, pas de message"
                    
                },
                message: {
                    required: "Saisir un message SVP",
                    minlength: "Fournir plus de détails SVP"
                   
                }
            }
            //removed  here!! 
        })
    })
        
 })(jQuery)
})