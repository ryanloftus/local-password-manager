const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = [
    {
        entry: './src/renderer.jsx',
        output: {
            filename: 'renderer.js',
            path: path.resolve(__dirname, 'dist'),
        },
        mode: 'development',
        target: 'electron-renderer',
        resolve: {
            extensions: ['', '.js', '.jsx'],
        },
        module: {
            rules: [
                {
                    test: /\.(jsx|js)$/,
                    include: path.resolve(__dirname, 'src'),
                    exclude: /node_modules/,
                    use: [{
                        loader: 'babel-loader',
                        options: {
                            presets: [
                                ['@babel/preset-env', {
                                    "targets": "defaults"
                                }],
                                '@babel/preset-react'
                            ]
                        }
                    }]
                },
                {
                    test: /\.css$/,
                    use: [
                        'style-loader',
                        { loader: 'css-loader', options: { importLoaders: 1 } },
                    ],
                },
            ]
        },
        plugins: [
            new HtmlWebpackPlugin({
                template: './src/index.html'
            })
        ],
    },
    {
        entry: './src/electron.js',
        output: {
            filename: 'electron.js',
            path: path.resolve(__dirname, 'dist'),
        },
        mode: 'development',
        target: 'electron-main',
    }
];
