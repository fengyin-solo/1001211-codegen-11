import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const VesselBerth = () => import('@/views/vessel_berth/index.vue')
const QuayCrane = () => import('@/views/quay_crane/index.vue')
const Container = () => import('@/views/container/index.vue')
const YardSlot = () => import('@/views/yard_slot/index.vue')
const YardCrane = () => import('@/views/yard_crane/index.vue')
const Truck = () => import('@/views/truck/index.vue')
const Gate = () => import('@/views/gate/index.vue')
const Dangerous = () => import('@/views/dangerous/index.vue')
const Reefer = () => import('@/views/reefer/index.vue')
const PowerStation = () => import('@/views/power_station/index.vue')
const Stevedore = () => import('@/views/stevedore/index.vue')
const Tariff = () => import('@/views/tariff/index.vue')
const Tide = () => import('@/views/tide/index.vue')
const Accident = () => import('@/views/accident/index.vue')
const Equipment = () => import('@/views/equipment/index.vue')
const Pilot = () => import('@/views/pilot/index.vue')
const Customs = () => import('@/views/customs/index.vue')
const ShiftLog = () => import('@/views/shift_log/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/vessel_berth', name: 'vessel_berth', component: VesselBerth },
    { path: '/quay_crane', name: 'quay_crane', component: QuayCrane },
    { path: '/container', name: 'container', component: Container },
    { path: '/yard_slot', name: 'yard_slot', component: YardSlot },
    { path: '/yard_crane', name: 'yard_crane', component: YardCrane },
    { path: '/truck', name: 'truck', component: Truck },
    { path: '/gate', name: 'gate', component: Gate },
    { path: '/dangerous', name: 'dangerous', component: Dangerous },
    { path: '/reefer', name: 'reefer', component: Reefer },
    { path: '/power_station', name: 'power_station', component: PowerStation },
    { path: '/stevedore', name: 'stevedore', component: Stevedore },
    { path: '/tariff', name: 'tariff', component: Tariff },
    { path: '/tide', name: 'tide', component: Tide },
    { path: '/accident', name: 'accident', component: Accident },
    { path: '/equipment', name: 'equipment', component: Equipment },
    { path: '/pilot', name: 'pilot', component: Pilot },
    { path: '/customs', name: 'customs', component: Customs },
    { path: '/shift_log', name: 'shift_log', component: ShiftLog },
  ],
})

export default router
