
// module.exports = {
//     devServer: {
//         host: 'localhost',
//         port: 8080,
//     proxy:{
//         "server":{
//             target:"http://localhost:5000",
//             ws:true,
//             changeOrigin:true,
//             pathRewrite:{
//                 '^/server':''
//             }
//             }
//     }
//     }
// }

module.exports = {
    devServer: {
        proxy: {
            '/api': {
                // target: 'http://1.117.221.135:5000/', //接口域名
                target: 'http://127.0.0.1:5000', //接口域名
                changeOrigin: true,             //是否跨域
                ws: true,                       //是否代理 websockets
                secure: true,                   //是否https接口
                pathRewrite: {                  //路径重置
                    '^/api': ''
                }
            }
        }
    }
};
