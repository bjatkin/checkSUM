const path = require('path');

module.exports = {
    entry: {
		bundle: ['./src/main.js']
	},
    resolve: {
        alias: {
            svelte: path.resolve('node_modules', 'svelte')
        },
        extensions: ['.mjs', '.js', '.svelte'],
        mainFields: ['svelte', 'browser', 'module', 'main']
    },
    output: {
		path: __dirname + '/public',
		filename: '[name].js',
		chunkFilename: '[name].[id].js'
	},
    module: {
        rules: [
            {
                test: /\.(html|svelte)$/,
                exclude: /node_modules/,
                use: 'svelte-loader'
            }
        ]
    }
}