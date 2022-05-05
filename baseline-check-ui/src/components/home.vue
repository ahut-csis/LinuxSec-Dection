<template>
    <el-container class="home-container">
        <!-- 头部区域 -->
        <el-header>
            <div style="display: flex;align-items: center;">
                <img src="../assets/ahut.png" alt="" style="height: 50px">
                <span style="margin-left: 15px;">AHUT-CSIS等保检查</span>
            </div>
            <el-button type="info" @click="logout">退出</el-button>
        </el-header>
        <!-- 页面主体区域 -->
        <el-container>
            <!-- 侧边栏 -->
            <el-aside :width="'200px'">
                <!-- 侧边栏菜单区域 -->
                <el-menu background-color="#333744" text-color="#fff" active-text-color="#409EFF"  >
                    <el-menu-item index="1">
                        <i class="el-icon-s-home"></i>
                        <span slot="title" @click="saveNavState('/welcome')">首页</span>
                    </el-menu-item>
                    <el-submenu index="2">
                        <template slot="title">
                            <i class="el-icon-menu"></i>
                            <span>Linux操作系统</span>
                        </template>
                        <el-submenu index="2-1">
                            <template slot="title">主机配置检查</template>
                            <el-menu-item index="2-1-1" @click="saveNavState('/linuxcheck')" >1.基本信息</el-menu-item>
                            <el-menu-item index="2-1-2" @click="saveNavState('/empty')">2.账户信息</el-menu-item>
                            <el-menu-item index="2-1-3" @click="saveNavState('/checkphoto')">3.可视化大屏</el-menu-item>
                            <el-menu-item index="2-1-4" @click="saveNavState('/empty')">4.生成总体报告</el-menu-item>
                        </el-submenu>
                        <el-menu-item-group>
                            <el-menu-item index="2-2" @click="saveNavState('/empty')" >安全基线配置管理</el-menu-item>
                        </el-menu-item-group>
                        <el-menu-item-group>
                            <el-menu-item index="2-3" @click="saveNavState('/empty')" >安全核查和分析判别</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>

                    <el-submenu index="3">
                        <template slot="title">
                            <i class="el-icon-menu"></i>
                            <span>Windows操作系统</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="1-1" @click="saveNavState('/empty')" >基本信息查询</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>
                    <el-submenu index="4">
                        <template slot="title">
                            <i class="el-icon-coin"></i>
                            <span>数据库</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="1-1" @click="saveNavState('/empty')" >基本信息查询</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>
                    <el-submenu index="5">
                        <template slot="title">
                            <i class="el-icon-s-tools"></i>
                            <span>扩展</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="1-1" @click="saveNavState('/checklist')" >支撑的安全检查主机与数据列表</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>

                </el-menu>
            </el-aside>
            <!-- 右侧内容主体 -->
            <el-main>
                <!-- 路由占位符 -->
                <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    export default {
        data() {
            return {

            }
        },
        created() {
        },
        methods: {
            logout() {
                this.$router.push('/index')
            },
            saveNavState(activePath) {
                this.$router.push(activePath)
            }

        }
    }
</script>

<style scoped>
    .home-container {
        height: 100%;
    }
    .el-header {
        background-color: #373d41;
        display: flex;
        justify-content: space-between;
        padding-left: 0;
        align-items: center;
        color: #fff;
        font-size: 20px;

    }

    .el-aside {
        background-color: #333744;

    }

    .el-main {
        background-color: #eaedf1;
    }

    .iconfont {
        margin-right: 10px;
    }

    .toggle-button {
        background-color: #4a5064;
        font-size: 10px;
        line-height: 24px;
        color: #fff;
        text-align: center;
        letter-spacing: 0.2em;
        cursor: pointer;
    }
</style>
