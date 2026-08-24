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
    'WaveNode is the AI-powered video and audio streaming platform for creators, developers and enterprises. Go live in minutes with a global low-latency network, AI captions, monetization tools and a developer-first API.',
    'Go live in minutes with a global low-latency network, AI captions, monetization tools and a developer-first API.',
)

register(
    'features.html',
    'Features — WaveNode AI Video &amp; Audio Streaming Platform',
    'Explore every WaveNode capability: global low-latency streaming, audio rooms, meetings, AI captions and translation, automatic highlight clips, monetization, recordings and real-time analytics.',
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
