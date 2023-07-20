/* Connect to orders_app in main_app.html */
new Vue ({
    el: '#events',
    data: {
    orders: []
    },
    created: function() {
        /* Code js. Argument 'this' means when Vue will created it will placed in 'this' */
        const vm = this;
        axios.get('/api/event/')
        /* Then means after finishing previous */
        .then(function (response){
        vm.events = response.data
        })
    }
}

)