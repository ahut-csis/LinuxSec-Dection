<template>
  <div>
    <h3 style="width: 100%;vertical-align: middle; height: 100%;">Welcome to Ahut-CISI</h3>

    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :md="24" :lg="11" :xl="11">
        <el-card class="card" shadow="never">
          <div slot="header">
            <span>依赖信息</span>
            <div style="float: right">2022-3-8 11:45:19</div>
          </div>

          <div class="bottom-btn">
            <a
                    target="_blank"
                    href="https://github.com/chuzhixin/vue-admin-better"
            >
              <el-button type="warning" style="margin: 5px 10px 15px 0;">github下载源码点star</el-button>
            </a>
          </div>


          <table class="table">
            <tr>
              <td class="">vue/cli版本</td>
              <td class="">3.4.5</td>
              <td>vue版本</td>
              <td>3.4.6</td>
            </tr>
            <tr>
              <td>vuex版本</td>
              <td>3.6</td>
              <td>vue-router版本</td>
              <td>2.0.1</td>
            </tr>
            <tr>
              <td>element-ui版本</td>
              <td>1.5.2</td>
              <td>axios版本</td>
              <td>2.3.4</td>
            </tr>
            <tr>
              <td>eslint版本</td>
              <td>3.4.5</td>
              <td>prettier版本</td>
              <td>3.4.5</td>
            </tr>
            <tr>
              <td>sass版本</td>
              <td>3.4.5</td>
              <td>mockjs版本</td>
              <td>3.4.5</td>
            </tr>
            <tr>
              <td>zx-layouts版本</td>
              <td>3.4.5</td>
              <td>lodash版本</td>
              <td>3.4.5</td>
            </tr>
          </table>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<style>
  .table {
    width: 100%;
    color: #666;
    border-collapse: collapse;
    background-color: #fff;
  }
</style>