<template>
    <div id="page" class="gg-page">
        <div class="responsive-menu">
            <nav>

                <ul class="main-menu" id="menu_mobile" data-indicate-active="starts-with">
                    <li>
                        <a href="/">
                            <span class="icon-general"></span>
                            All eSports
                        </a>
                    </li>
                </ul>
                <ul class="sub-menu" data-indicate-active>

                    <li><a href="/tournaments">Tournaments</a></li>
                    <li><a href="/matches">Matches</a></li>
                    <li><a href="/rankings">Rankings</a></li>
                    <li><a href="/streams">Streams</a></li>
                    <li><a href="/vods">VODs</a></li>

                </ul>
            </nav>
        </div>

        <main class="main-wrap row">

            <div class="large-15 columns">
                <div class="row">

                </div>
            </div>


            <div class="content large-15 columns">
                <section id="bannerSet" class="module featured row">
                    <div class="large-5 columns" v-for="league of topLeagues" :key="league.league_id">
                        <div class="row">
                            <a :href="`/league/${league.uri_name}`">
                                <i class="event-icon icon-dota2"></i> {{league.name}}
                            </a>
                        </div>
                    </div>
                </section>
                <div class="row">
                    <div class="left large-4 columns">

                        <section class="module news row">
                            <h1>
                                <i class="icon-general"></i>
                                eSports news
                            </h1>


                            <article class="news-post display-vertical has-thumbnail" v-for="news in stringToDate(topNews)" :key="news.article_id">
                                <a class="post-thumbnail" :href="`/news/${news.article_id}`">
                                    <img alt="Fnatic take another win for SEA at ESL One Birmingham 2020 "
                                         src="https://static.gosugamers.net/264x_/61/80/b8/b2b4fb1b2d78aa99fa29286a4dd96d6ef89b6f4f78901883cd5761de61.jpg">
                                </a>
                                <div class="post-content">
                                    <a :href="`/news/${news.article_id}`">
                                        <h4 class="post-title">
                                            {{news.title}}
                                        </h4>
                                    </a>
                                    <div class="post-details">
                                        <a href="/game/dota2" class="post-section">
                                            <i class="icon-dota2"></i>
                                            Dota 2
                                        </a>
                                        <span class="post-date">
                                            <time class="relative" :datetime="`${news.created_date}`">
                                                {{news.created_date}}
                                            </time>
                                        </span>
                                        <span>Đặng Nhật Anh</span>
                                    </div>
                                </div>
                            </article>


                            <a href="/articles" class="view-more arrow green button">
                                More news
                            </a>
                        </section>
                    </div>
                    <div class="right-block large-11 columns">
                        <div class="row flex-layout">
                            <div class="center large-7 columns">

                                <section class="module main-video row">
                                    <div class="wrap">


                                        <iframe src="https://player.twitch.tv/?channel=esea&autoplay=false&muted=false"
                                                allowfullscreen>
                                        </iframe>


                                    </div>



                                    <div class="large-15 columns">
                                        <div class="row">
                                            <a href="/counterstrike/tournaments/39046-esea-season-34/matches/356741-movistar-riders-vs-pro100"
                                               class="match live">
                                                <div class="details text-center hide-for-small-only medium-7 medium-push-4 columns">
                                                    <div class="row">
                                                        <span class="time">Live</span>
                                                        <span class="event">
                                                            ESEA Season 34
                                                        </span>
                                                    </div>
                                                </div>
                                                <div class="team team-1 small-7 medium-4 medium-pull-7 columns">
                                                    <div class="row">
                                                        <div class="avatar"
                                                             style="background-image:url('https://static.gosugamers.net/100x100/ba/f3/d3/76b8e413457cd9a30990220fb543de6ced812851c179232a8bbdb1be72.png');">
                                                        </div>
                                                        <div class="name">Movistar Riders</div>
                                                        <div class="region">
                                                            <span class="flag flag-es"
                                                                  title="Spain"
                                                                  data-tooltip
                                                                  tabindex="1"></span>

                                                            Spain
                                                        </div>
                                                        <small class="meta">Rank 43</small>
                                                    </div>
                                                </div>
                                                <div class="team team-2 small-7 medium-4 columns">
                                                    <div class="row">
                                                        <div class="avatar"
                                                             style="background-image:url('https://static.gosugamers.net/100x100/7a/03/e8/febc7c0f1479c34bf5aa2ce8441b4a681922c40e1ce2460dea3978617c.png');">
                                                        </div>
                                                        <div class="name">PRO100</div>
                                                        <div class="region">
                                                            <span class="flag flag-ru"
                                                                  title="Russian Federation"
                                                                  data-tooltip
                                                                  tabindex="1"></span>

                                                            Russian Federation
                                                        </div>
                                                        <small class="meta">Rank 94</small>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                    </div>
                                </section>
                                <div class="row flex-layout">
                                    <div class="large-8 columns">

                                        <section class="module editorial row">
                                            <h3>Editorial</h3>


                                            <article class="news-post display-vertical has-thumbnail">
                                                <a class="post-thumbnail" href="/dota2/features/51992-independent-streamers-vs-tournament-organizers">
                                                    <img alt="Independent streamers vs Tournament Organizers"
                                                         src="https://static.gosugamers.net/264x_/15/c4/36/52154c95e6435c990e184f76a80834a35c09d73e0df6968e38f0814dec.jpg">
                                                </a>
                                                <div class="post-content">
                                                    <a href="/dota2/features/51992-independent-streamers-vs-tournament-organizers">
                                                        <h4 class="post-title">
                                                            Independent streamers vs Tournament Organizers
                                                        </h4>
                                                    </a>
                                                    <div class="post-details">
                                                        <a href="/dota2" class="post-section">
                                                            <i class="icon-dota2"></i>
                                                            Dota 2
                                                        </a>
                                                        <span class="post-date">
                                                            <time class="relative" datetime="2020-05-14T11:49:03+02:00">
                                                                5/14/20, 11:49 AM
                                                            </time>
                                                        </span>
                                                        <span>Pandoradota2</span>
                                                    </div>
                                                </div>
                                            </article>




                                            <article class="news-post display-vertical has-thumbnail">
                                                <a class="post-thumbnail" href="/dota2/features/51770-dpc-season-interrupted-what-now">
                                                    <img alt="DPC season interrupted; What now?"
                                                         src="https://static.gosugamers.net/264x_/08/eb/fa/90a996b5e3a4c780431799c2a341c2d910cb3abcacd42df5bfbb8c9cdf.jpg">
                                                </a>
                                                <div class="post-content">
                                                    <a href="/dota2/features/51770-dpc-season-interrupted-what-now">
                                                        <h4 class="post-title">
                                                            DPC season interrupted; What now?
                                                        </h4>
                                                    </a>
                                                    <div class="post-details">
                                                        <a href="/dota2" class="post-section">
                                                            <i class="icon-dota2"></i>
                                                            Dota 2
                                                        </a>
                                                        <span class="post-date">
                                                            <time class="relative" datetime="2020-04-16T19:30:00+02:00">
                                                                4/16/20, 7:30 PM
                                                            </time>
                                                        </span>
                                                        <span>Pandoradota2</span>
                                                    </div>
                                                </div>
                                            </article>




                                            <article class="news-post display-vertical has-thumbnail">
                                                <a class="post-thumbnail" href="/dota2/features/51409-weplay-mad-moon-out-of-this-world">
                                                    <img alt="WePlay! Mad Moon out of this world"
                                                         src="https://static.gosugamers.net/264x_/53/49/6d/4a3951088d8a595ca3391f91f455e69fd69d8a31174830178375496bf3.jpg">
                                                </a>
                                                <div class="post-content">
                                                    <a href="/dota2/features/51409-weplay-mad-moon-out-of-this-world">
                                                        <h4 class="post-title">
                                                            WePlay! Mad Moon out of this world
                                                        </h4>
                                                    </a>
                                                    <div class="post-details">
                                                        <a href="/dota2" class="post-section">
                                                            <i class="icon-dota2"></i>
                                                            Dota 2
                                                        </a>
                                                        <span class="post-date">
                                                            <time class="relative" datetime="2020-02-27T09:08:12+01:00">
                                                                2/27/20, 9:08 AM
                                                            </time>
                                                        </span>
                                                        <span>Pandoradota2</span>
                                                    </div>
                                                </div>
                                            </article>


                                            <a href="/features" class="view-more arrow green button">
                                                More articles
                                            </a>
                                        </section>
                                    </div>
                                    <div class="large-7 columns">
                                        <section class="row module tournaments">
                                            <h3>Tournaments</h3>
                                            <ul>
                                                <li>
                                                    <a href="/overwatch/tournaments/39051-overwatch-league-season-3" class="event">
                                                        <div class="block-img" style="background-image:url('https://static.gosugamers.net/248x_/ab/f8/13/859f422823690c2e9662944d4eb86040ec1a17bfa949a260cf97abefea.png');"></div>
                                                        <div class="has-tip" title="Overwatch League Season 3" data-tooltip tabindex="1">
                                                            Overwatch League Season...
                                                        </div>
                                                        <small>
                                                            Overwatch tournament
                                                        </small>
                                                    </a>
                                                </li>
                                                <li>
                                                    <a href="/counterstrike/tournaments/38162-esl-one-rio-2020" class="event">
                                                        <div class="block-img" style="background-image:url('https://static.gosugamers.net/248x_/24/69/25/6d7296ebf479f4319f50d94df07b4479214ea14dc19f504ed25a94573c.png');"></div>
                                                        <div class="has-tip">
                                                            ESL One: Rio 2020
                                                        </div>
                                                        <small>
                                                            CS:GO tournament
                                                        </small>
                                                    </a>
                                                </li>
                                                <li>
                                                    <a href="/overwatch/tournaments/36472-overwatch-contenders-2020-season-1" class="event">
                                                        <div class="block-img" style="background-image:url('https://static.gosugamers.net/248x_/ce/0a/c7/19c101e36d83cfa0a1e5b7f9f745e9bbcebc4d1289f98592e937b696c5.png');"></div>
                                                        <div class="has-tip"
                                                             title="Overwatch Contenders 2020 Season 1"
                                                             data-tooltip
                                                             tabindex="1">
                                                            Overwatch Contenders 202...
                                                        </div>
                                                        <small>
                                                            Overwatch tournament
                                                        </small>
                                                    </a>
                                                </li>
                                                <li>
                                                    <a href="/lol/tournaments/39410-eu-community-showdown-2020" class="event">
                                                        <div class="block-img" style="background-image:url('https://static.gosugamers.net/248x_/68/40/49/e52e36ab2b2a6b56e6962a013a520494aad8826c44e3d34546fc274084.jpg');"></div>
                                                        <div class="has-tip"
                                                             title="EU Community Showdown 2020"
                                                             data-tooltip
                                                             tabindex="1">
                                                            EU Community Showdown 20...
                                                        </div>
                                                        <small>
                                                            LoL tournament
                                                        </small>
                                                    </a>
                                                </li>
                                                <li>
                                                    <a href="/counterstrike/tournaments/38047-blast-premier-fall-2020" class="event">
                                                        <div class="block-img" style="background-image:url('https://static.gosugamers.net/248x_/3c/61/a6/a3754eba133003eb5c10f129d2be3bc65798bb2177f8e5d30b1bf2e007.png');"></div>
                                                        <div class="has-tip">
                                                            BLAST Premier: Fall 2020
                                                        </div>
                                                        <small>
                                                            CS:GO tournament
                                                        </small>
                                                    </a>
                                                </li>
                                                <li>
                                                    <a href="/counterstrike/tournaments/38003-esl-one-cologne-2020" class="event">
                                                        <div class="block-img" style="background-image:url('https://static.gosugamers.net/248x_/51/9e/ac/8daf74c5da2eacc417557c233e57306426f44ebdc50a8256fe5366cbb8.png');"></div>
                                                        <div class="has-tip">
                                                            ESL One: Cologne 2020
                                                        </div>
                                                        <small>
                                                            CS:GO tournament
                                                        </small>
                                                    </a>
                                                </li>
                                            </ul>
                                            <a href="/tournaments"
                                               class="view-more arrow green button">
                                                More tournaments
                                            </a>
                                        </section>
                                        <section class="top-rankings module row">
                                            <h3>Rankings</h3>
                                            <a href="/rankings"
                                               class="view-more arrow green button">
                                                GosuGamers Rankings
                                            </a>
                                        </section>

                                    </div>
                                </div>
                            </div>
                            <div class="right large-4 columns">
                                <section class="module matchticker row">
                                    <h3 class="float-left">Matchticker</h3>
                                    <ul class="tabs float-right" data-load-target=".matchticker .tabs-content ul">
                                        <li class="tabs-title is-active">
                                            <a href="/matchticker/upcoming"
                                               id="matchtickerUpcomingTab"
                                               aria-selected="true">
                                                Schedule
                                            </a>
                                        </li>
                                        <li class="tabs-title">
                                            <a href="/matchticker/results"
                                               id="matchtickerResultsTab">
                                                Results
                                            </a>
                                        </li>
                                    </ul>
                                    <div class="tabs-content">
                                        <div class="tabs-panel scrollbar-macosx is-active">
                                            <ul>
                                                <li></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <a href="/matches"
                                       class="view-more sliding secondary button expanded">
                                        All matches
                                    </a>
                                </section>
                                <div class="box-container">
                                    <div id="boxTopWrapper">
                                        <div id="slot-3">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="welcome"
                 class="reveal welcome-reveal"
                 data-reveal
                 data-animation-in="fade-in"
                 data-animation-out="fade-out"
                 data-close-button
                 data-deep-link="true"
                 data-gg-href="/welcome">
            </div>

        </main>

        <Footer/>
    </div>
</template>

<script>
    import Footer from './Footer.vue'
    import axios from 'axios'
    import moment from 'moment'
    export default {
        name: 'Home',
        props: {
            msg: String
        },
        components: {Footer},
        data() {
            return {
                topLeagues: [],
                leagues: [],
                topNews: [],
                news: [],
                loading: true
            }
        },
        methods: {
            stringToDate: (lst) => {
                for (var item in lst) {
                    console.log(lst)
                    item.created_date = moment(String(item.created_date)).format('MM/DD/YYYY')
                }
                return lst
            }
        },
        mounted() {
            axios
                .get('https://esportapi.helisoft.vn/api/leagues/')
                .then(response => {
                    if (response.status === 200) {
                        this.topLeagues = response.data.results.slice(0, 3)
                        this.leagues = response.data.results
                    }
                })
                .finally(() => this.loading = false)
            axios
                .get('https://esportapi.helisoft.vn/api/articles/')
                .then(response => {
                    if (response.status === 200) {
                        this.topNews = response.data.results.slice(0, 3)
                        this.news = response.data.results
                    }
                })
                .finally(() => this.loading = false)
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
