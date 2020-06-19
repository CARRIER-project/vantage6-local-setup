--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2 (Debian 12.2-2.pgdg100+1)
-- Dumped by pg_dump version 12.2 (Debian 12.2-2.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Member; Type: TABLE; Schema: public; Owner: vantage
--

CREATE TABLE public."Member" (
    organization_id integer,
    collaboration_id integer
);


ALTER TABLE public."Member" OWNER TO vantage;

--
-- Name: authenticatable; Type: TABLE; Schema: public; Owner: vantage
--

CREATE TABLE public.authenticatable (
    id integer NOT NULL,
    type character varying(50),
    ip character varying,
    last_seen timestamp without time zone,
    status character varying
);


ALTER TABLE public.authenticatable OWNER TO vantage;

--
-- Name: authenticatable_id_seq; Type: SEQUENCE; Schema: public; Owner: vantage
--

CREATE SEQUENCE public.authenticatable_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authenticatable_id_seq OWNER TO vantage;

--
-- Name: authenticatable_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vantage
--

ALTER SEQUENCE public.authenticatable_id_seq OWNED BY public.authenticatable.id;


--
-- Name: collaboration; Type: TABLE; Schema: public; Owner: vantage
--

CREATE TABLE public.collaboration (
    id integer NOT NULL,
    name character varying,
    encrypted boolean
);


ALTER TABLE public.collaboration OWNER TO vantage;

--
-- Name: collaboration_id_seq; Type: SEQUENCE; Schema: public; Owner: vantage
--

CREATE SEQUENCE public.collaboration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.collaboration_id_seq OWNER TO vantage;

--
-- Name: collaboration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vantage
--

ALTER SEQUENCE public.collaboration_id_seq OWNED BY public.collaboration.id;


--
-- Name: node; Type: TABLE; Schema: public; Owner: vantage
--

CREATE TABLE public.node (
    id integer NOT NULL,
    name character varying,
    api_key character varying,
    collaboration_id integer,
    organization_id integer
);


ALTER TABLE public.node OWNER TO vantage;

--
-- Name: organization; Type: TABLE; Schema: public; Owner: vantage
--

CREATE TABLE public.organization (
    id integer NOT NULL,
    name character varying,
    domain character varying,
    address1 character varying,
    address2 character varying,
    zipcode character varying,
    country character varying,
    _public_key bytea
);


ALTER TABLE public.organization OWNER TO vantage;

--
-- Name: organization_id_seq; Type: SEQUENCE; Schema: public; Owner: vantage
--

CREATE SEQUENCE public.organization_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organization_id_seq OWNER TO vantage;

--
-- Name: organization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vantage
--

ALTER SEQUENCE public.organization_id_seq OWNED BY public.organization.id;


--
-- Name: result; Type: TABLE; Schema: public; Owner: vantage
--

CREATE TABLE public.result (
    id integer NOT NULL,
    input text,
    task_id integer,
    organization_id integer,
    result text,
    assigned_at timestamp without time zone,
    started_at timestamp without time zone,
    finished_at timestamp without time zone,
    log text
);


ALTER TABLE public.result OWNER TO vantage;

--
-- Name: result_id_seq; Type: SEQUENCE; Schema: public; Owner: vantage
--

CREATE SEQUENCE public.result_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.result_id_seq OWNER TO vantage;

--
-- Name: result_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vantage
--

ALTER SEQUENCE public.result_id_seq OWNED BY public.result.id;


--
-- Name: task; Type: TABLE; Schema: public; Owner: vantage
--

CREATE TABLE public.task (
    id integer NOT NULL,
    name character varying,
    description character varying,
    image character varying,
    collaboration_id integer,
    run_id integer,
    parent_id integer,
    database character varying,
    initiator_id integer
);


ALTER TABLE public.task OWNER TO vantage;

--
-- Name: task_id_seq; Type: SEQUENCE; Schema: public; Owner: vantage
--

CREATE SEQUENCE public.task_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.task_id_seq OWNER TO vantage;

--
-- Name: task_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vantage
--

ALTER SEQUENCE public.task_id_seq OWNED BY public.task.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: vantage
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying,
    password character varying,
    firstname character varying,
    lastname character varying,
    roles character varying,
    organization_id integer
);


ALTER TABLE public."user" OWNER TO vantage;

--
-- Name: authenticatable id; Type: DEFAULT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.authenticatable ALTER COLUMN id SET DEFAULT nextval('public.authenticatable_id_seq'::regclass);


--
-- Name: collaboration id; Type: DEFAULT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.collaboration ALTER COLUMN id SET DEFAULT nextval('public.collaboration_id_seq'::regclass);


--
-- Name: organization id; Type: DEFAULT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.organization ALTER COLUMN id SET DEFAULT nextval('public.organization_id_seq'::regclass);


--
-- Name: result id; Type: DEFAULT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.result ALTER COLUMN id SET DEFAULT nextval('public.result_id_seq'::regclass);


--
-- Name: task id; Type: DEFAULT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.task ALTER COLUMN id SET DEFAULT nextval('public.task_id_seq'::regclass);


--
-- Data for Name: Member; Type: TABLE DATA; Schema: public; Owner: vantage
--

COPY public."Member" (organization_id, collaboration_id) FROM stdin;
1	1
\.


-- --
-- -- Data for Name: authenticatable; Type: TABLE DATA; Schema: public; Owner: vantage
-- --
--
COPY public.authenticatable (id, type, ip, last_seen, status) FROM stdin;
2	user	\N	\N	\N
1	user	172.28.0.1	2020-06-11 13:18:06.657867	\N
3	user	172.28.0.1	2020-06-11 13:18:07.086026	\N
5	node	\N	\N	\N
4	user	172.28.0.1	2020-06-11 13:18:07.31515	\N
6	node	\N	\N	\N
8	node	\N	\N	\N
7	node	\N	\N	\N
\.


--
-- Data for Name: collaboration; Type: TABLE DATA; Schema: public; Owner: vantage
--

COPY public.collaboration (id, name, encrypted) FROM stdin;
1	collab1	f
\.


--
-- Data for Name: node; Type: TABLE DATA; Schema: public; Owner: vantage
--

COPY public.node (id, name, api_key, collaboration_id, organization_id) FROM stdin;
7	NLEsC - collab1 Node	56b97dd2-aefa-11ea-a535-0242ac130005	1	1
\.


--
-- Data for Name: organization; Type: TABLE DATA; Schema: public; Owner: vantage
--

COPY public.organization (id, name, domain, address1, address2, zipcode, country, _public_key) FROM stdin;
1	NLEsC	\N	my address 1, Amsterdam	\N	1234ab	the Netherlands	\\x
\.


--
-- Data for Name: result; Type: TABLE DATA; Schema: public; Owner: vantage
--

COPY public.result (id, input, task_id, organization_id, result, assigned_at, started_at, finished_at, log) FROM stdin;
\.


--
-- Data for Name: task; Type: TABLE DATA; Schema: public; Owner: vantage
--

COPY public.task (id, name, description, image, collaboration_id, run_id, parent_id, database, initiator_id) FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: vantage
--

COPY public."user" (id, username, password, firstname, lastname, roles, organization_id) FROM stdin;
1	root	$2b$12$sw0bC7xWL7IO8JzyriDfU.8MQoZOpJoJCw4H4heaBPJLlqhIk6Ngu	\N	\N	root	\N
2	admin	$2b$12$CDI8HGZrDZv55NKe9ooZre8r6lIYY79hs3SQBfcPHJFhBV2oQXrJK	djura	smits	admin	1
3	admin_2	$2b$12$gQ8Tf02NzKdvkf49/nKvvepF9vbvg2t3625BgJfBjTwOdhoafhdgy	djura	smits	admin	2
4	admin_3	$2b$12$8CTAlFNpb4QwZGPPNOAnyewlRXQXzWuiP0MSo60WK4lAy4hQ6Lr4O	djura	smits	admin	3
\.


--
-- Name: authenticatable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vantage
--

SELECT pg_catalog.setval('public.authenticatable_id_seq', 6, true);


--
-- Name: collaboration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vantage
--

SELECT pg_catalog.setval('public.collaboration_id_seq', 1, true);


--
-- Name: organization_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vantage
--

SELECT pg_catalog.setval('public.organization_id_seq', 3, true);


--
-- Name: result_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vantage
--

SELECT pg_catalog.setval('public.result_id_seq', 1, false);


--
-- Name: task_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vantage
--

SELECT pg_catalog.setval('public.task_id_seq', 1, false);


--
-- Name: authenticatable authenticatable_pkey; Type: CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.authenticatable
    ADD CONSTRAINT authenticatable_pkey PRIMARY KEY (id);


--
-- Name: collaboration collaboration_pkey; Type: CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.collaboration
    ADD CONSTRAINT collaboration_pkey PRIMARY KEY (id);


--
-- Name: node node_pkey; Type: CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.node
    ADD CONSTRAINT node_pkey PRIMARY KEY (id);


--
-- Name: organization organization_pkey; Type: CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.organization
    ADD CONSTRAINT organization_pkey PRIMARY KEY (id);


--
-- Name: result result_pkey; Type: CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.result
    ADD CONSTRAINT result_pkey PRIMARY KEY (id);


--
-- Name: task task_pkey; Type: CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: Member Member_collaboration_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_collaboration_id_fkey" FOREIGN KEY (collaboration_id) REFERENCES public.collaboration(id);


--
-- Name: Member Member_organization_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_organization_id_fkey" FOREIGN KEY (organization_id) REFERENCES public.organization(id);


--
-- Name: node node_collaboration_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.node
    ADD CONSTRAINT node_collaboration_id_fkey FOREIGN KEY (collaboration_id) REFERENCES public.collaboration(id);


--
-- Name: node node_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.node
    ADD CONSTRAINT node_id_fkey FOREIGN KEY (id) REFERENCES public.authenticatable(id);


--
-- Name: node node_organization_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.node
    ADD CONSTRAINT node_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES public.organization(id);


--
-- Name: result result_organization_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.result
    ADD CONSTRAINT result_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES public.organization(id);


--
-- Name: result result_task_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.result
    ADD CONSTRAINT result_task_id_fkey FOREIGN KEY (task_id) REFERENCES public.task(id);


--
-- Name: task task_collaboration_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_collaboration_id_fkey FOREIGN KEY (collaboration_id) REFERENCES public.collaboration(id);


--
-- Name: task task_initiator_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_initiator_id_fkey FOREIGN KEY (initiator_id) REFERENCES public.organization(id);


--
-- Name: task task_parent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES public.task(id);


--
-- Name: user user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_id_fkey FOREIGN KEY (id) REFERENCES public.authenticatable(id);


--
-- Name: user user_organization_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vantage
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES public.organization(id);


--
-- PostgreSQL database dump complete
--

