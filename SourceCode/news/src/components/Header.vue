<template>
    <header class="header">
        <div class="header-wrap grid-x">
            <a class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </a>
            <router-link class="logo cell" to="/">
                <div class="g-logo">
                    <div>
                        <img src="https://www.gosugamers.net/assets/images/app/site/logos/gosu-logo-b6c6c4d6.png" />
                    </div>
                </div>
                <div class="game" style="background-image:url('https://www.gosugamers.net/assets/images/app/site/logos/gosugamers/logo-general-df89458c.png')">
                    <img src="https://www.gosugamers.net/assets/images/app/site/logos/gosugamers/logo-general-df89458c.png" />
                </div>
            </router-link>
            <nav class="menu cell shrink">

                <ul class="main-menu" id="menu_desktop" data-indicate-active="starts-with">
                    <li class="is-active">
                        <router-link to="/">
                            All eSports
                        </router-link>
                    </li>
                    <li v-for="game in games" :key="game.game_id">
                        <router-link class="logo cell" :to="`/${game.uri_name}`">
                            {{ game.name }}
                        </router-link>
                    </li>
                </ul>
                <ul class="sub-menu" data-indicate-active>

                    <li><a href="/tournaments">Tournaments</a></li>
                    <li><a href="/matches">Matches</a></li>
                    <li><a href="/rankings">Rankings</a></li>
                    <!--<li><a href="/streams">Streams</a></li>
                    <li><a href="/vods">VODs</a></li>-->

                </ul>
            </nav>
        </div>
        <div style="display:none" class="user-menu grid-x hover-submenu">
            <a href="/login?from=%2F" class="rounded green button">Login</a>
        </div>
    </header>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Header',
        props: {
            msg: String
        },
        data() {
            return {
                games: null,
                loading: true
            }
        },
        mounted() {
            axios
                .get('https://esportapi.helisoft.vn/api/games/')
                .then(response => {
                    if (response.status === 200) {
                        this.games = response.data.results
                    }
                })
                .finally(() => this.loading = false)
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    /*header*/

    .header {
        transition: .3s .3s cubic-bezier(.86,0,.07,1);
        transition-delay: 0s;
        position: fixed;
        justify-content: center;
        background-position: top;
        display: flex;
        flex-wrap: wrap;
        z-index: 3;
        top: 0;
        left: 0;
        width: 100%;
        min-height: 100px;
        box-shadow: 0 0 20px rgba(0,0,0,.5);
    }

    body .header {
        background-image: url(https://www.gosugamers.net/assets/images/app/site/backgrounds/general-df0bd9ef.jpg);
    }

    .header::before {
        content: "";
        position: absolute;
        right: 0;
        width: 50%;
        height: 100%;
        background-color: #27282d;
    }

    .header .header-wrap {
        min-width: 1140px;
    }

    .header .hamburger {
        width: 30px;
        height: 30px;
        display: block;
        position: absolute;
        cursor: pointer;
        left: 50%;
        top: 15px;
    }

        .header .hamburger span {
            transition: all .3s cubic-bezier(.86,0,.07,1);
            border-radius: 2px;
            width: 100%;
            height: 4px;
            position: absolute;
            left: 0;
            background-color: #737682;
        }

            .header .hamburger span:nth-of-type(1) {
                top: 3px;
                transform-origin: top left;
            }

            .header .hamburger span:nth-of-type(2) {
                top: 13px;
            }

            .header .hamburger span:nth-of-type(3) {
                top: 23px;
                transform-origin: bottom left;
            }

    .header .logo {
        padding-right: 40px;
        padding-top: 15px;
        padding-bottom: 15px;
        display: flex;
        justify-content: flex-start;
        width: auto;
        align-items: stretch;
    }

        .header .logo.responsive .g-logo {
            margin-left: 20px;
        }

        .header .logo .g-logo {
            transition: all .3s cubic-bezier(.86,0,.07,1);
            max-width: 70px;
        }

            .header .logo .g-logo img {
                display: block;
            }

    .header.fixed .logo .g-logo {
        max-width: 32px;
    }

    .header .logo.responsive .game {
        max-width: 0;
    }

    .header.fixed .logo .game {
        max-width: 0;
        transition-delay: 0s;
    }

    .header .logo .game {
        transition: .3s .3s cubic-bezier(.86,0,.07,1);
        transition-delay: .3s;
        overflow: hidden;
        transform: scaleX(1);
        max-width: 160px;
        transform-origin: left;
        background-position: center left;
        background-repeat: no-repeat;
    }

        .header .logo .game img {
            width: auto;
            opacity: 0;
        }

    .header .menu {
        font-family: 'Roboto Condensed', sans-serif;
        text-transform: uppercase;
        font-weight: 600;
        margin-top: 4px;
        font-size: 14px;
        line-height: 14px;
        display: flex;
        flex-direction: column;
        width: auto;
        margin: 0;
        position: relative;
        background-color: #27282d;
    }

        .header .menu::before {
            content: "";
            position: absolute;
            width: 30px;
            height: 100px;
            bottom: 0;
            right: 100%;
            border-right: 30px solid #27282d;
            border-top: 100px solid transparent;
        }

    .header ul {
        list-style: none;
        margin: 0;
    }

    .header .main-menu {
        transition: .3s .3s cubic-bezier(.86,0,.07,1);
        transition-delay: 0s;
        display: flex;
        text-transform: none;
        font-weight: 400;
        box-sizing: border-box;
        overflow: hidden;
        height: 40px;
        border-bottom: 1px solid #343437;
    }

    .header .menu a {
        color: #9698a3;
    }

    .header .main-menu li a {
        padding: 0 10px;
        height: 39px;
        line-height: 40px;
    }

    .header .main-menu .is-active a {
        color: #f7f7f0;
        background-color: transparent;
    }

    .header .main-menu li::after {
        transition: all .5s cubic-bezier(.215,.61,.355,1);
        content: "";
        margin: -3px 10px 0;
        display: block;
        opacity: 0;
        border-bottom: 3px solid #ab8569;
    }

    .header .main-menu .is-active::after, .header .main-menu li:hover::after {
        opacity: 1;
    }

    .header .sub-menu {
        display: flex;
        height: 59px;
        margin-left: -10px;
    }

        .header .sub-menu li {
            display: flex;
        }

        .header .sub-menu a {
            display: flex;
            padding: 0 10px;
            flex-grow: 1;
            justify-content: center;
            align-items: center;
        }

    .header .menu a:hover {
        color: #f7f7f0;
    }

    .header.fixed .user-menu {
        height: 60px;
        transition-delay: .3s;
    }

    .user-menu {
        transition: all .3s cubic-bezier(.86,0,.07,1);
        position: absolute;
        z-index: 1;
        right: 0;
        bottom: 0;
        height: 100px;
        display: flex;
        padding: 0 20px;
        align-items: center;
        transition-delay: 0;
    }
</style>
