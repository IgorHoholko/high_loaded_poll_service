--
-- PostgreSQL data_distributor dump
--

-- Dumped from data_distributor version 13.1 (Debian 13.1-1.pgdg100+1)
-- Dumped by pg_dump version 13.1 (Debian 13.1-1.pgdg100+1)

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

--
-- Name: demo; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA demo;


ALTER SCHEMA demo OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: g; Type: TABLE; Schema: demo; Owner: postgres
--

CREATE TABLE demo.g (
    id integer
);


ALTER TABLE demo.g OWNER TO postgres;

--
-- Name: answers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.answers (
    id integer NOT NULL,
    text character varying(40) NOT NULL,
    question_id integer NOT NULL
);


ALTER TABLE public.answers OWNER TO postgres;

--
-- Name: questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.questions (
    id integer NOT NULL,
    text character varying(200) NOT NULL
);


ALTER TABLE public.questions OWNER TO postgres;

--
-- Name: user_answer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_answer (
    id integer NOT NULL,
    user_id integer NOT NULL,
    answer_id integer NOT NULL
);


ALTER TABLE public.user_answer OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(40) NOT NULL,
    nickname character varying(40) NOT NULL,
    language_code character varying(40) NOT NULL,
    is_bot boolean NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Data for Name: g; Type: TABLE DATA; Schema: demo; Owner: postgres
--

COPY demo.g (id) FROM stdin;
\.


--
-- Data for Name: answers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.answers (id, text, question_id) FROM stdin;
1	Liverpool	1
2	Manchester City	1
3	Arsenal	1
\.


--
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.questions (id, text) FROM stdin;
1	Which club won the 1986 FA Cup Final?
\.


--
-- Data for Name: user_answer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_answer (id, user_id, answer_id) FROM stdin;
1	1	2
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, nickname, language_code, is_bot) FROM stdin;
1	Pavel	Pasha1	RU	f
2	Olga Ivanova	olechka44	RU	f
3	Alexander Petrov	alex_alex	EN	f
4	Roman Pupkin	roma_pup	BY	f
\.


--
-- Name: answers answer_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.answers
    ADD CONSTRAINT answer_id PRIMARY KEY (id);


--
-- Name: users id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT id PRIMARY KEY (id);


--
-- Name: questions question_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT question_id PRIMARY KEY (id);


--
-- Name: user_answer user_answer_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_answer
    ADD CONSTRAINT user_answer_id PRIMARY KEY (id);


--
-- Name: users users_nickname_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_nickname_key UNIQUE (nickname);


--
-- Name: user_answer a_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_answer
    ADD CONSTRAINT a_id FOREIGN KEY (answer_id) REFERENCES public.answers(id);


--
-- Name: answers q_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.answers
    ADD CONSTRAINT q_id FOREIGN KEY (question_id) REFERENCES public.questions(id);


--
-- Name: user_answer u_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_answer
    ADD CONSTRAINT u_id FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL data_distributor dump complete
--

