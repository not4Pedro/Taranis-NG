<template>
  <v-app-bar
    dense
    flat
    class="main-menu-bar bg-cx-app-header pr-0 pl-0"
    :height="48"
    app
    clipped-left
  >
    <template #prepend>
      <v-btn color="primary" @click.stop="navClicked">
        <v-icon
          :class="['menu-icon', { closed: !drawerVisible }]"
          icon="mdi-menu-open"
        />
      </v-btn>
    </template>

    <v-toolbar-title>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        version="1.1"
        height="30"
        viewBox="0 0 435 84"
      >
        <g id="taranis-logo">
          <path
            fill="var(--color-1)"
            d="M355.998,61.705l-32,0l-4,-4l0,-8l8,0l0,4l24,0l0,-8l-28,0l-4,-4l0,-16l4,-4l32,0l4,4l0,8l-8,0l0,-4l-24,0l0,8l28,0l4,4l0,16l-4,4Zm-42,0l-8,0l0,-40l8,0l0,40Zm-92,0l-8,0l0,-40l26,0l14,14l0,26l-8,0l0,-8l-24,0l0,8Zm-60,0l-8,0l0,-8l-24,0l0,8l-8,0l0,-26l14,-14l26,0l0,40Zm106,0l-8,0l0,-40l8,0l24,28l0,-28l8,0l0,40l-8,0l-24,-28l0,28Zm-92,0l-8,0l0,-40l32,0l8,8l0,16l-4,4l4,4l0,8l-8,0l0,-4l-4,-4l-20,0l0,8Zm-54,-32l-16,0l0,32l-8,0l0,-32l-16,0l0,-8l40,0l0,8Zm302.795,-2c1.217,0 2.205,0.988 2.205,2.205l0,23.591c0,1.216 -0.988,2.204 -2.205,2.204l-45.591,0c-1.216,0 -2.204,-0.988 -2.204,-2.204l0,-23.591c0,-1.217 0.988,-2.205 2.204,-2.205l45.591,0Zm-270.795,2l-14,0l-10,10l0,6l24,0l0,-16Zm42,0l-20,0l0,16l20,0l4,-4l0,-8l-4,-4Zm40,0l-14,0l0,16l24,0l0,-6l-10,-10Z"
          />
          <path
            fill="var(--color-2)"
            d="M420.998,31.705l2,2l0,4l-4,0l0,-2l-12,0l0,12l12,0l0,-4l-6,0l0,-4l10,0l0,12l-18,0l-2,-2l0,-16l2,-2l16,0Zm-36,20l-4,0l0,-20l4,0l12,14l0,-14l4,0l0,20l-4,0l-12,-14l0,14Z"
          />
          <path
            fill="var(--color-3)"
            d="M51.249,31.04c-1.668,-2.343 -1.452,-5.619 0.648,-7.72c2.342,-2.341 6.144,-2.341 8.486,0c2.341,2.342 2.341,6.144 0,8.486c-2.101,2.1 -5.377,2.316 -7.72,0.648l-4.345,4.345c2.238,2.877 2.238,6.935 0,9.812l4.345,4.345c2.343,-1.668 5.619,-1.452 7.72,0.649c2.341,2.341 2.341,6.143 0,8.485c-2.101,2.101 -5.377,2.317 -7.72,0.648l-4.345,4.346c2.441,3.137 2.219,7.68 -0.663,10.562c-3.122,3.122 -8.192,3.122 -11.314,0c-3.122,-3.122 -3.122,-8.191 0,-11.313c2.883,-2.883 7.426,-3.104 10.563,-0.664l4.345,-4.345c-1.477,-2.074 -1.477,-4.88 0,-6.953l-4.345,-4.346c-3.137,2.441 -7.68,2.22 -10.563,-0.663c-1.306,-1.306 -2.066,-2.954 -2.279,-4.657l-12.412,0c-0.213,1.703 -0.973,3.351 -2.28,4.657c-3.122,3.122 -8.191,3.122 -11.313,0c-3.122,-3.122 -3.122,-8.192 0,-11.314c3.122,-3.122 8.191,-3.122 11.313,0c1.307,1.307 2.067,2.954 2.28,4.657l12.412,0c0.213,-1.703 0.973,-3.35 2.279,-4.657c2.883,-2.882 7.426,-3.103 10.563,-0.663l4.345,-4.345Zm-13.494,34.707c2.342,-2.342 6.144,-2.342 8.486,0c2.341,2.341 2.341,6.144 0,8.485c-2.342,2.342 -6.144,2.342 -8.486,0c-2.341,-2.341 -2.341,-6.144 0,-8.485Zm-15.556,-15.557c3.122,-3.122 8.192,-3.122 11.314,0c3.122,3.123 3.122,8.192 0,11.314c-3.122,3.122 -8.192,3.122 -11.314,0c-3.122,-3.122 -3.122,-8.191 0,-11.314Zm1.414,1.415c2.342,-2.342 6.144,-2.342 8.485,0c2.342,2.341 2.342,6.143 0,8.485c-2.341,2.342 -6.143,2.342 -8.485,0c-2.341,-2.342 -2.341,-6.144 0,-8.485Zm41.012,-15.557c3.122,-3.122 8.192,-3.122 11.314,0c3.122,3.122 3.122,8.192 0,11.314c-3.122,3.122 -8.192,3.122 -11.314,0c-3.122,-3.122 -3.122,-8.192 0,-11.314Zm1.415,1.415c2.341,-2.342 6.143,-2.342 8.485,0c2.341,2.341 2.341,6.143 0,8.485c-2.342,2.341 -6.144,2.341 -8.485,0c-2.342,-2.342 -2.342,-6.144 0,-8.485Zm-28.285,0c2.342,-2.342 6.144,-2.342 8.486,0c2.341,2.341 2.341,6.143 0,8.485c-2.342,2.341 -6.144,2.341 -8.486,0c-2.341,-2.342 -2.341,-6.144 0,-8.485Zm-28.284,0c2.342,-2.342 6.144,-2.342 8.485,0c2.342,2.341 2.342,6.143 0,8.485c-2.341,2.341 -6.143,2.341 -8.485,0c-2.342,-2.342 -2.342,-6.144 0,-8.485Zm26.207,-19.136c-2.441,-3.137 -2.22,-7.68 0.663,-10.563c3.122,-3.122 8.192,-3.122 11.314,0c3.122,3.122 3.122,8.192 0,11.314c-2.883,2.882 -7.426,3.104 -10.563,0.663l-4.345,4.345c1.668,2.343 1.452,5.619 -0.649,7.72c-2.341,2.341 -6.143,2.341 -8.485,0c-2.341,-2.342 -2.341,-6.144 0,-8.486c2.101,-2.1 5.377,-2.316 7.72,-0.648l4.345,-4.345Zm2.077,-9.149c2.342,-2.341 6.144,-2.341 8.486,0c2.341,2.342 2.341,6.144 0,8.486c-2.342,2.341 -6.144,2.341 -8.486,0c-2.341,-2.342 -2.341,-6.144 0,-8.486Z"
          />
        </g>
      </svg>
    </v-toolbar-title>

    <div v-if="showItemCount" class="mr-10">
      <span>
        total items: <strong>{{ itemCountTotal }}</strong>
      </span>
      <span v-if="isFiltered">
        / displayed items: <strong>{{ itemCountFiltered }}</strong>
      </span>
    </div>

    <template #append>
      <v-toolbar color="transparent">
        <div v-for="button in buttonList" :key="button.route">
          <v-btn variant="text" :ripple="false" :to="button.route">
            <v-icon left>{{ button.icon }}</v-icon>
            <span class="main-menu-item">
              {{ $t(button.title) }}
            </span>
          </v-btn>
        </div>
        <user-menu />
      </v-toolbar>
    </template>
  </v-app-bar>
</template>

<script>
import UserMenu from '@/components/UserMenu.vue'

import { storeToRefs } from 'pinia'
import { useMainStore } from '@/stores/MainStore'
import { defineComponent, computed } from 'vue'
import { useI18n } from 'vue-i18n'

export default defineComponent({
  name: 'MainMenu',
  components: { UserMenu },
  setup() {
    const store = useMainStore()
    const { d } = useI18n()

    store.updateFromLocalConfig()

    const { drawerVisible, itemCountTotal, itemCountFiltered, buildDate } =
      storeToRefs(store)

    const showItemCount = computed(() => {
      return itemCountTotal.value !== undefined && itemCountTotal.value > 0
    })

    const isFiltered = computed(() => {
      return itemCountFiltered.value === undefined
        ? false
        : itemCountFiltered.value !== itemCountTotal.value
    })

    const navClicked = () => {
      store.toggleDrawer()
    }
    const buttons = [
      {
        title: 'main_menu.dashboard',
        icon: 'mdi-monitor-dashboard',
        permission: 'ASSESS_ACCESS',
        route: '/',
        show: true
      },
      {
        title: 'main_menu.administration',
        icon: 'mdi-cog-outline',
        permission: 'CONFIG_ACCESS',
        route: '/config',
        show: true
      },
      {
        title: 'main_menu.enter',
        icon: 'mdi-location-enter',
        permission: 'ASSESS_CREATE',
        route: '/enter',
        show: false
      },
      {
        title: 'main_menu.assess',
        icon: 'mdi-google-circles-extended',
        permission: 'ASSESS_ACCESS',
        route: '/assess',
        show: true
      },
      {
        title: 'main_menu.analyze',
        icon: 'mdi-google-circles-communities',
        permission: 'ANALYZE_ACCESS',
        route: '/analyze',
        show: true
      },
      {
        title: 'main_menu.publish',
        icon: 'mdi-publish',
        permission: 'PUBLISH_ACCESS',
        route: '/publish',
        show: true
      },
      {
        title: 'main_menu.assets',
        icon: 'mdi-file-multiple-outline',
        permission: 'MY_ASSETS_ACCESS',
        route: '/assets',
        show: true
      }
    ]

    const buttonList = computed(() => {
      return buttons.filter(
        (button) =>
          store.user.permissions.includes(button.permission) && button.show
      )
    })

    return {
      d,
      buildDate,
      isFiltered,
      showItemCount,
      itemCountFiltered,
      itemCountTotal,
      drawerVisible,
      buttonList,
      navClicked
    }
  }
})
</script>
