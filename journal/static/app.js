/* Connect to view.events in events.html */
new Vue ({
    el: '#events',
//    Inside view will see:
    data: {
    events: []
    },
    created: function() {
        /* Code js. Argument 'this' means when Vue will created it will placed in 'this' same as __str__(self)*/
        const vm = this;
        axios.get('/api/event/')
        /* Then means after finishing previous */
        .then(function (response){
        vm.events = response.data
        })
    }
}

)