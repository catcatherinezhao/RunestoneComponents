var tieList = {};    // Dictionary that contains all instances of TIE objects

Tie.prototype = new RunestoneBase();

// Define Tie object
function Tie (opts) {
    if (opts) {
        this.init(opts);
    }
}

/*======================================
== Initialize basic TIE attributes ==
========================================*/
Tie.prototype.init = function (opts) {
    RunestoneBase.apply(this, arguments);
    RunestoneBase.prototype.init.apply(this, arguments);

    var orig = opts.orig;     // entire <div> element that will be replaced by new HTML
    this.origElem = orig;
    this.divid = orig.id;

    this.origContent = $(this.origElem).html();
    
    this.renderHTML();
};

Tie.prototype.renderHTML = function() {
    this.containerDiv = document.createElement("div");
    this.containerDiv.id = this.divid;
    $(this.containerDiv).addClass(this.origElem.getAttribute("class"));
    this.newLearnerViewDirective = document.createElement("learner-view");
    this.containerDiv.appendChild(this.newLearnerViewDirective);

    $(this.origElem).replaceWith(this.containerDiv);
};
    /*var html = "<div>" +
                "    <learner-view-directive>" +
                "    </learner-view-directive>" +
                "</div>";*/

/*=================================
== Find the custom HTML tags and ==
==     execute our code on them        ==
=================================*/
$(document).ready(function () {
    $("[data-component=tie]").each(function (index) {
        tieList[this.id] = new Tie({"orig": this});
    });
});

if (typeof component_factory === 'undefined') {
    component_factory = {}
}
component_factory['tie'] = function(opts) { return new Tie(opts)}
