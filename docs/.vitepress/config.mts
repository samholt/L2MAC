import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  markdown: {
    math: true,
  },
  title: "L2MAC",
  base: "/L2MAC/",
  description: "The LLM Automatic Computer Framework",
  lastUpdated: true,
  themeConfig: {
    logo: '/l2mac-icon.png',
    editLink: {
      pattern: 'https://github.com/samholt/L2MAC/blob/master/docs/:path'
    },
    search: {
      provider: 'local',
    },
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      {
        text: 'Docs',
        link: '/guide/get_started/introduction',
        activeMatch: '/get_started/',
      },
      {
        text: 'Mission',
        link: '/guide/mission',
      },
      {
        text: 'Gallery',
        link: '/guide/use_cases/gallery',
      },
    ],

    sidebar: {
      '/guide/': {
        base: '/guide/',
        items: [
      {
        text: 'Get Started',
        collapsed: false,
        items: [
          { text: 'Introduction', link: 'get_started/introduction' },
          { text: 'Quickstart', link: 'get_started/quickstart' },
          { text: 'Installation', link: 'get_started/installation' },
          {
            text: 'Configuration',
            link: 'get_started/configuration',
            items: [
              {
                text: 'LLM',
                link: 'get_started/configuration/llm_api_configuration',
              },
            ],
          },
          {
            text: 'Comparison to AutoGPT',
            link: 'get_started/comparison_to_autogpt',
          },
        ],
      },
      {
        text: 'Tutorials',
        collapsed: false,
        items: [
          { text: 'Concepts', link: 'tutorials/concepts' },
          { text: 'L2MAC 101', link: 'tutorials/l2mac_101' },
        ],
      },
      {
        text: 'Use Cases',
        collapsed: false,
        items: [
          {
            text: 'Gallery of Examples',
            link: 'use_cases/gallery',
          },
          {
            text: 'Codebase Generator',
            link: 'use_cases/codebase_generator',
          },
          {
            text: 'Book Generator',
            link: 'use_cases/book_generator',
          },
        ],
      },
      {
        text: 'Contribute',
        collapsed: false,
        items: [
          {
            text: 'Contribute guide',
            link: 'contribute/contribute_guide',
          },
        ],
      },
      {
        text: 'Mission',
        link: 'mission',
      },
      {
        text: 'Roadmap',
        link: 'roadmap',
      },
      {
        text: 'API',
        link: 'api',
      },
      {
        text: 'FAQ',
        link: 'faq',
      },
      ],
      }
    },

    
    socialLinks: [
      { icon: 'github', link: 'https://github.com/samholt/l2mac' },
      { icon: 'discord', link: 'https://discord.gg/z27CxnwdhY' },
      { icon: 'x', link: 'https://twitter.com/samianholt' },
      // { icon: 'linkedin', link: 'https://uk.linkedin.com/in/samuel-holt' },
      { icon: {
        svg: '<svg fill="#000000" height="800px" width="800px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve"><g><g><path d="M256,0C114.62,0,0,114.62,0,256s114.62,256,256,256s256-114.62,256-256S397.38,0,256,0z M172.211,41.609 c-24.934,27.119-44.68,66.125-56.755,111.992H49.749C75.179,102.741,118.869,62.524,172.211,41.609z M25.6,256 c0-26.999,5.077-52.727,13.662-76.8h70.494c-4.608,24.294-7.356,49.963-7.356,76.8s2.748,52.506,7.347,76.8H39.262 C30.677,308.727,25.6,283,25.6,256z M49.749,358.4h65.707c12.083,45.867,31.821,84.872,56.755,111.991 C118.869,449.476,75.179,409.259,49.749,358.4z M243.2,485.188c-43.81-8.252-81.877-58.24-101.359-126.788H243.2V485.188z  M243.2,332.8H135.74c-4.924-24.166-7.74-49.997-7.74-76.8s2.816-52.634,7.74-76.8H243.2V332.8z M243.2,153.6H141.841 C161.323,85.052,199.39,35.063,243.2,26.812V153.6z M462.251,153.6h-65.707c-12.083-45.867-31.821-84.873-56.755-111.992 C393.131,62.524,436.821,102.741,462.251,153.6z M268.8,26.812c43.81,8.252,81.877,58.24,101.359,126.788H268.8V26.812z  M268.8,179.2h107.46c4.924,24.166,7.74,49.997,7.74,76.8s-2.816,52.634-7.74,76.8H268.8V179.2z M268.8,485.188V358.4h101.359 C350.677,426.948,312.61,476.937,268.8,485.188z M339.789,470.391c24.934-27.127,44.672-66.125,56.755-111.991h65.707 C436.821,409.259,393.131,449.476,339.789,470.391z M402.244,332.8c4.608-24.294,7.356-49.963,7.356-76.8 s-2.748-52.506-7.347-76.8h70.494c8.576,24.073,13.653,49.801,13.653,76.8c0,27-5.077,52.727-13.662,76.8H402.244z"/></g></g></svg>'
      },
            link: "https://samholt.github.io/",
            ariaLabel: 'Personal Website'},
      { icon: {
        svg: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><!--!Font Awesome Free 6.5.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M320 32c-8.1 0-16.1 1.4-23.7 4.1L15.8 137.4C6.3 140.9 0 149.9 0 160s6.3 19.1 15.8 22.6l57.9 20.9C57.3 229.3 48 259.8 48 291.9v28.1c0 28.4-10.8 57.7-22.3 80.8c-6.5 13-13.9 25.8-22.5 37.6C0 442.7-.9 448.3 .9 453.4s6 8.9 11.2 10.2l64 16c4.2 1.1 8.7 .3 12.4-2s6.3-6.1 7.1-10.4c8.6-42.8 4.3-81.2-2.1-108.7C90.3 344.3 86 329.8 80 316.5V291.9c0-30.2 10.2-58.7 27.9-81.5c12.9-15.5 29.6-28 49.2-35.7l157-61.7c8.2-3.2 17.5 .8 20.7 9s-.8 17.5-9 20.7l-157 61.7c-12.4 4.9-23.3 12.4-32.2 21.6l159.6 57.6c7.6 2.7 15.6 4.1 23.7 4.1s16.1-1.4 23.7-4.1L624.2 182.6c9.5-3.4 15.8-12.5 15.8-22.6s-6.3-19.1-15.8-22.6L343.7 36.1C336.1 33.4 328.1 32 320 32zM128 408c0 35.3 86 72 192 72s192-36.7 192-72L496.7 262.6 354.5 314c-11.1 4-22.8 6-34.5 6s-23.5-2-34.5-6L143.3 262.6 128 408z"/></svg>'
      },
        link: 'https://scholar.google.com/citations?hl=en&user=Ey5aInIAAAAJ&view_op=list_works&sortby=pubdate',
        ariaLabel: 'Google Scholar'},
      { icon: {
        svg: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--!Font Awesome Free 6.5.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M48 64C21.5 64 0 85.5 0 112c0 15.1 7.1 29.3 19.2 38.4L236.8 313.6c11.4 8.5 27 8.5 38.4 0L492.8 150.4c12.1-9.1 19.2-23.3 19.2-38.4c0-26.5-21.5-48-48-48H48zM0 176V384c0 35.3 28.7 64 64 64H448c35.3 0 64-28.7 64-64V176L294.4 339.2c-22.8 17.1-54 17.1-76.8 0L0 176z"/></svg>'
      },
        link: 'https://samholt.github.io/#contact',
        ariaLabel: 'Contact'},

        ],
    footer: {
          message: 'Released under the MIT License.',
          copyright: 'Copyright © 2023-present Sam Holt'
        }
      },
  head: [
    ['link', { rel: 'icon', href: '/L2MAC/favicon.ico' }],
    [
      'script',
      { async: '', src: 'https://www.googletagmanager.com/gtag/js?id=G-TXHDRXTGTW' }
    ],
    [
      'script',
      {},
      `window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-TXHDRXTGTW');`
    ]
  ]
})
