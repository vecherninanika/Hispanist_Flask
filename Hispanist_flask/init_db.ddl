CREATE EXTENSION "uuid-ossp";

CREATE TABLE IF NOT EXISTS users   (id uuid primary key default uuid_generate_v4(), 
                                    full_name TEXT NOT NULL,
                                    login TEXT NOT NULL,
                                    email TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS topics   (id uuid primary key default uuid_generate_v4(),
                                    title TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS users_to_topics (id uuid primary key default uuid_generate_v4(),
                                        user_id uuid references users,
                                        topic_id uuid references topics);

CREATE UNIQUE INDEX users_topic_idx ON users__to_topics (user_id, topic_id);

CREATE TABLE IF NOT EXISTS resourses   (id uuid primary key default uuid_generate_v4(), 
                                      title TEXT NOT NULL,
                                      type TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS resourses_to_topics (id uuid primary key default uuid_generate_v4(),
                                           resourse_id uuid references resourses,
                                           topic_id uuid references topics);

CREATE UNIQUE INDEX users_topic_idx ON resourses_to_topics (resourse_id, topic_id);

CREATE TABLE IF NOT EXISTS eayh_questions  (id uuid primary key default uuid_generate_v4(), 
                                            question TEXT NOT NULL,
                                            options TEXT[] NOT NULL,
                                            answer TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS schools  (id uuid primary key default uuid_generate_v4(), 
                                    name TEXT NOT NULL,
                                    place INT NOT NULL,
                                    website TEXT);

drop table universitys;

CREATE TABLE IF NOT EXISTS universities  (id uuid primary key default uuid_generate_v4(), 
                                        name TEXT NOT NULL,
                                        place INT NOT NULL,
                                        website TEXT);
