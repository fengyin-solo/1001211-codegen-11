<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "船舶靠泊", "created": 0, "pending": 0, "abnormal": 0}, {"name": "岸桥作业", "created": 0, "pending": 0, "abnormal": 0}, {"name": "集装箱信息", "created": 0, "pending": 0, "abnormal": 0}, {"name": "堆场箱位", "created": 0, "pending": 0, "abnormal": 0}, {"name": "场桥调度", "created": 0, "pending": 0, "abnormal": 0}, {"name": "内集卡调度", "created": 0, "pending": 0, "abnormal": 0}, {"name": "闸口管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "危险品监管", "created": 0, "pending": 0, "abnormal": 0}, {"name": "冷藏箱监控", "created": 0, "pending": 0, "abnormal": 0}, {"name": "供电桩管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "装卸队管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "费率结算", "created": 0, "pending": 0, "abnormal": 0}, {"name": "潮汐气象", "created": 0, "pending": 0, "abnormal": 0}, {"name": "事故处置", "created": 0, "pending": 0, "abnormal": 0}, {"name": "设备保养", "created": 0, "pending": 0, "abnormal": 0}, {"name": "引航调度", "created": 0, "pending": 0, "abnormal": 0}, {"name": "海关查验", "created": 0, "pending": 0, "abnormal": 0}, {"name": "工班日志", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
