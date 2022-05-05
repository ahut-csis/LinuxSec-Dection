<template>
    <div class="container">
        <div>

            <h2 class="title">
                AHUT-CSIC: 等保核查
            </h2>

            <div class="links">
                <el-button  class="button--green" @click="login">
                        进入demo
                </el-button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        methods: {
            login() {
                this.$router.push('/home')
            }
        }
    }
</script>

<style>
    .container {
        margin: 0 auto;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        background-color: antiquewhite;
    }


    .title {
        font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        display: block;
        font-weight: 300;
        font-size: 36px;
        color: #35495e;
        letter-spacing: 1px;
        word-spacing: 5px;
        margin: 20px 0;
    }


    .links {
        padding-top: 15px;
    }

    .button--green {
        display: inline-block;
        border-radius: 4px;
        border: 1px solid #3b8070;
        color: #3b8070;
        text-decoration: none;
        padding: 10px 30px;
    }

    .button--green:hover {
        color: #fff;
        background-color: #3b8070;
    }

    .button--grey {
        display: inline-block;
        border-radius: 4px;
        border: 1px solid #35495e;
        color: #35495e;
        text-decoration: none;
        padding: 10px 30px;
        margin-left: 15px;
    }




</style>