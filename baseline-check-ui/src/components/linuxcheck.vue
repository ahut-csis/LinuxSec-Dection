<template>
    <div>
        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>Linux操作系统</el-breadcrumb-item>
        </el-breadcrumb>

        <el-card>
            <!-- 搜索与添加区域 -->
            <el-form :inline="true" :model="formInline" class="demo-form-inline">
                <el-form-item label="Id地址">
                    <el-input v-model="formInline.ip" placeholder="Id地址"></el-input>
                </el-form-item>
                <el-form-item label="用户名">
                    <el-input v-model="formInline.user" placeholder="用户名"></el-input>
                </el-form-item>
                <el-form-item label="密码">
                    <el-input v-model="formInline.password" type="password" placeholder="密码"></el-input>
                </el-form-item>
                <el-form-item label="端口号">
                    <el-input v-model="formInline.port" placeholder="端口号"></el-input>
                </el-form-item>


                <el-form-item>
                    <el-button type="primary" @click="getMenuList(formInline.ip,formInline.user,formInline.password,formInline.port)">查询</el-button>
                </el-form-item>
            </el-form>

            <div>
                <span>CPU信息:</span>
                <span>{{this.cpu}}</span>
            </div>
            <div style="height: 10px"></div>
            <div>
                <span>计算机名:</span>
                <span>{{this.hostname}}</span>
            </div>
            <div style="height: 10px"></div>
            <div>
                <span>内核版本:</span>
                <span>{{this.uname}}</span>
            </div>
            <div style="height: 10px"></div>
            <div>
                <span>内存信息:</span>
                <span>{{this.meminfo}}</span>
            </div>
            <div style="height: 10px"></div>
            <div>
                <span>操作系统类型:</span>
                <span>{{this.ostype}}</span>
            </div>
            <div style="height: 10px"></div>
            <div>
                <span>网卡MAC地址:</span>
                <span>{{this.macip}}</span>
            </div>


        </el-card>
    </div>



</template>

<script>
    export default {
        data() {
            return {
                formInline: {
                    ip:'',
                    port:22,
                    user: '',
                    password: ''
                },
                cpu:'',
                hostname:'',
                uname:'',
                meminfo:'',
                ostype:'',
                macip:''
            }
        },
        created() {
        },
        methods: {
            onSubmit() {
                console.log('submit!');
            },
            async getMenuList(ip,user,pass,port) {
                let params = 'hostname='+ip+'&username='+user+'&password='+pass+'&port='+port;
                const { data: res } = await this.$http.get('/api/GetOsBase?'+params);
                console.log(res.cpu);
                this.cpu=res.cpu;
                this.hostname=res.hostname;
                this.uname=res.uname;
                this.meminfo=res.meminfo;
                this.ostype=res.ostype;
                this.macip=res.macip;
            },
        }
    }
</script>

<style>



</style>