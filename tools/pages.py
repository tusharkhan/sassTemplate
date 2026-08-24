# WaveNode page registry — read by build.py.
#
# register(filename, title, description, og_description,
#          active=<nav href to highlight>, cta=<include CTA banner>,
#          shell='site' | 'auth')
#
# Keep this list in the same order the pages appear in the navbar.

register(
    'index.html',
    'WaveNode — AI-Powered Video &amp; Audio Streaming API Platform',
    'WaveNode is the AI-powered video and audio streaming platform for creators, developers and enterprises. Go live in minutes with a global low-latency network, AI captions, monetisation tools and a developer-first API.',
    'Go live in minutes with a global low-latency network, AI captions, monetisation tools and a developer-first API.',
)

register(
    'features.html',
    'Features — WaveNode AI Video &amp; Audio Streaming Platform',
    'Explore every WaveNode capability: global low-latency streaming, audio rooms, meetings, AI captions and translation, automatic highlight clips, monetisation, recordings and real-time analytics.',
    'Live streaming, audio rooms, meetings and an AI toolkit — all behind one developer-first API.',
    active='features.html',
)

register(
    'pricing.html',
    'Pricing — WaveNode AI Video &amp; Audio Streaming Platform',
    'Simple, metered pricing for WaveNode. Start free with 1,000 streaming minutes a month, then scale on the Creator or Business plan. Published overage rates and no per-seat charges.',
    'Start free, upgrade when your audience grows. Every plan includes the global edge network.',
    active='pricing.html',
)

register(
    'blog.html',
    'Blog — WaveNode AI Video &amp; Audio Streaming Platform',
    'Engineering write-ups, protocol deep dives and practical advice from the team building the WaveNode streaming network — including the post-mortems.',
    'Notes from the edge of live: engineering deep dives from the WaveNode team.',
    active='blog.html',
)

register(
    'blog-single.html',
    'Cutting glass-to-glass latency from 210ms to 47ms — WaveNode Blog',
    'How we rebuilt the WaveNode WebRTC pipeline — adaptive jitter buffering, encoder lookahead and forwarding hops — to take median glass-to-glass latency from 210ms down to 47ms.',
    'Every change we shipped to cut live latency by 78%, in the order the numbers improved.',
    active='blog.html',
)

register(
    'docs.html',
    'Documentation — WaveNode Streaming API v3',
    'WaveNode API v3 documentation: quickstart, authentication, client SDKs, rooms, tracks, recordings, webhooks, error codes and rate limits.',
    'Create a room, publish a track, subscribe a viewer. Three calls and you are live.',
    active='docs.html',
)

register(
    'contact.html',
    'Contact — WaveNode AI Video &amp; Audio Streaming Platform',
    'Get in touch with WaveNode about pricing, integrations, enterprise agreements or support. Median first response is under three hours on weekdays.',
    'Sales questions, architecture reviews or a bug you cannot reproduce — it all reaches a human.',
    active='contact.html',
    cta=False,
)

register(
    'login.html',
    'Sign in — WaveNode',
    'Sign in to your WaveNode dashboard to manage streams, rooms, recordings and API keys.',
    'Sign in to your WaveNode dashboard.',
    shell='auth',
)

register(
    'register.html',
    'Create your free account — WaveNode',
    'Create a free WaveNode account and get 1,000 streaming minutes a month, the full global edge network and every SDK. No credit card required.',
    'Start building free — 1,000 streaming minutes a month, no card required.',
    shell='auth',
)

register(
    'forgot-password.html',
    'Reset your password — WaveNode',
    'Request a password reset link for your WaveNode account.',
    'Reset your WaveNode password.',
    shell='auth',
)

# ---------------------------------------------------------------------------
# Footer-linked pages (not in the main navbar)
# ---------------------------------------------------------------------------

register(
    'index-creator.html',
    'For Creators — WaveNode Live Streaming, Clips &amp; Monetisation',
    'WaveNode for creators and influencers: 4K live streaming, automatic vertical highlight clips, AI captions in 42 languages, and subscriptions, tickets and tips with payouts in 38 currencies.',
    'Go live, get clips, get paid — a flat 3% platform fee and payouts in two business days.',
)

register(
    'index-enterprise.html',
    'For Enterprise — WaveNode Compliant Live Video Infrastructure',
    'WaveNode for business and enterprise: SOC 2 Type II, EU/US/APAC data residency, SSO and SCIM, audit logs, bring-your-own storage and a 99.99% uptime SLA with financial credits.',
    'Live infrastructure that passes procurement — SOC 2, data residency, SSO and a 99.99% SLA.',
)

register(
    'integrations.html',
    'Integrations — WaveNode Streaming Platform',
    'Connect WaveNode to the stack you already run: Datadog, Grafana, PagerDuty, Amazon S3, Cloudflare R2, Stripe, Adyen, Okta, Microsoft Entra ID, Slack, Zapier and more.',
    'Twenty-one first-party integrations, all configured from the dashboard without glue code.',
)

register(
    'changelog.html',
    'Changelog — WaveNode Streaming API',
    'Every WaveNode release, including breaking changes and deprecations. Breaking changes get 90 days of notice and a migration guide before enforcement.',
    'Everything we shipped, including the boring parts. Deprecations listed before they are enforced.',
)

register(
    'about.html',
    'About — WaveNode AI Video &amp; Audio Streaming Platform',
    'WaveNode is 84 people across Berlin, Singapore and Austin building low-latency streaming infrastructure. Our story, how we work, and the team accountable for the network.',
    'Building the future of real-time communication — because latency is a product decision.',
)

register(
    'careers.html',
    'Careers — Work at WaveNode',
    'Eleven open roles across infrastructure, machine learning, developer experience and go-to-market. Remote across 14 countries, compensated on-call, paid interview exercises.',
    'Work on infrastructure that cannot be rolled back. Eleven roles open across four teams.',
)

register(
    'testimonials.html',
    'Customers — WaveNode Case Studies &amp; Testimonials',
    'How 4,000+ teams use WaveNode, with the numbers they let us publish: latency, delivery cost, engineering headcount and peak concurrency across streaming, education, health and commerce.',
    'Live infrastructure gets judged on the bad day. These customers let us quote the specifics.',
)

register(
    'help-center.html',
    'Help Center — WaveNode Support &amp; Guides',
    'Guides, troubleshooting and answers for the WaveNode streaming platform, written by the team that maintains it. Search the knowledge base or contact support directly.',
    'Guides and troubleshooting written by the people who maintain the platform.',
)

register(
    'faq.html',
    'FAQ — WaveNode Frequently Asked Questions',
    'Twenty answers on getting started, streaming quality and latency, the AI captioning and highlights toolkit, billing and overage rates, and security and compliance.',
    'Questions answered properly — where a number is involved, we give the number.',
)

register(
    'terms.html',
    'Terms of Service — WaveNode',
    'The agreement between you and WaveNode covering platform use, accounts and API keys, acceptable use, plans and payment, service levels, content rights, termination and liability.',
    'The agreement covering platform use, payment, acceptable use and responsibilities.',
    cta=False,
)

register(
    'privacy.html',
    'Privacy Policy — WaveNode',
    'What WaveNode collects, why, where it is stored, how long it is kept and what you can ask us to do with it — including our position on AI processing and model training.',
    'What we collect, why, where it lives and what you can ask us to do with it.',
    cta=False,
)

# ---------------------------------------------------------------------------
# Utility and app-UI pages
# ---------------------------------------------------------------------------

register(
    '404.html',
    'Page not found — WaveNode',
    'The page you requested could not be found. Browse the WaveNode help center, documentation or feature pages instead.',
    'This frame never arrived — the page you asked for is not here.',
    cta=False,
)

register(
    'user-dashboard.html',
    'Dashboard — WaveNode',
    'The WaveNode project dashboard: active streams, total viewers, median latency, generated clips, recent broadcasts and webhook delivery status.',
    'Active streams, viewers, latency and recent broadcasts at a glance.',
    cta=False,
)
