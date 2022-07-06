const http = require('http')
const port = 3000

const server = http.createServer(function(req, res){
    res.write('hello NET2')
    res.end()
})

server.listen(port, function(error){
    if (error){
        console.log('Erreur !', error)
    } else {
        console.log('Server is Listening on  port = ' + port)
    }
})
