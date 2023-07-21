drop table reservations;
drop table rooms;
drop table users;

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    type_of_user VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    host_id INT NOT NULL,
    room_name VARCHAR(100) NOT NULL,
    number_of_residents VARCHAR(50) NOT NULL,
    price INT NOT NULL,
    AC VARCHAR(3) NOT NULL,
    Refrigerator VARCHAR(3) NOT NULL,
    FOREIGN KEY (host_id) REFERENCES users (user_id)
);

CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    room_id INT NOT NULL,
    guest_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms (room_id),
    FOREIGN KEY (guest_id) REFERENCES users (user_id)
);

INSERT INTO users (name, email, type_of_user, password)
VALUES
('first_g', 'first_g.com', 'guest', 1111), 
('first_h', 'first_h.com', 'host', 2222), 
('second-g', 'second_g.com', 'guest', 3333);

INSERT INTO rooms (host_id, room_name, number_of_residents, price, AC, Refrigerator)
VALUES
(1, 'luxury', 1, 1, 'no', 'yes'),
(2, 'vip', 2, 2, 'yes', 'no'),
(3, 'luxury vip', 3, 3, 'yes', 'yes');

INSERT INTO reservations (room_id, guest_id, check_in_date, check_out_date)
VALUES
(1, 1, '12.01.20', '13.01.20'),
(2, 1, '13.01.20', '14.01.20'),
(3, 3, '14.01.20', '15.01.20');


select r.guest_id, count(r.*) as res_count, u.name
	from reservations r, users u
	where u.user_id = r.guest_id
	group by r.guest_id, u.name
	order by res_count desc
	limit 1



