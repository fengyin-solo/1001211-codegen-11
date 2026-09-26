<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">港口集装箱作业调度管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">覆盖船舶靠离、岸桥装卸、堆场箱位、闸口进出、危险品监管、冷藏箱供电及费率结算的港口集装箱全流程作业后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "船舶靠泊", path: "/vessel_berth" }, { label: "岸桥作业", path: "/quay_crane" }, { label: "集装箱信息", path: "/container" }, { label: "堆场箱位", path: "/yard_slot" }, { label: "场桥调度", path: "/yard_crane" }, { label: "内集卡调度", path: "/truck" }, { label: "闸口管理", path: "/gate" }, { label: "危险品监管", path: "/dangerous" }, { label: "冷藏箱监控", path: "/reefer" }, { label: "供电桩管理", path: "/power_station" }, { label: "装卸队管理", path: "/stevedore" }, { label: "费率结算", path: "/tariff" }, { label: "潮汐气象", path: "/tide" }, { label: "事故处置", path: "/accident" }, { label: "设备保养", path: "/equipment" }, { label: "引航调度", path: "/pilot" }, { label: "海关查验", path: "/customs" }, { label: "工班日志", path: "/shift_log" }]
</script>
