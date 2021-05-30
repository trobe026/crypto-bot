module.exports = {
    'env': {
        'node': true,
        'es6': true,
        'mocha': true
    },
    'parser': 'babel-eslint',
    'parserOptions': {
        'sourceType': 'module',
        'allowImportExportEverywhere': true,
        'ecmaVersion': 11,
        'ecmaFeatures': {
            'experimentalObjectRestSpread': true
        }
    },
    'extends': 'eslint:recommended',
    'rules': {
        'indent': [
            'error',
            4
        ],
        'linebreak-style': [
            'error',
            'unix'
        ],
        'quotes': [
            'error',
            'single'
        ],
        'semi': [
            'error',
            'always'
        ],
        'keyword-spacing': [
            'error'
        ],
        'object-curly-spacing': [
            'error',
            'always'
        ],
        'no-trailing-spaces': [
            'error'
        ],
        'no-console': 'off'
    }
};