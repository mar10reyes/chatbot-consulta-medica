<?php

require_once('../database/DatabaseConnectot.php');

class UserDao
{

    // Connection instance
    private $connection;

    // table name
    private $table_name = "users";

    // table columns
    public $id;
    public $name;
    public $password;

    public function __construct($connection){
        $this->connection = $connection;
    }

    
    public function create($name, $password)
    {
        $query = 'INSERT INTO users(name, password) VALUES('.$name.', '.$password.')';
        $stmt = $this->connection->prepare($query);
        $stmt->execute();

        return $stmt;
    }
    
    public function read($id){
        $query = 'SELECT * FROM users WHERE id='.$id;
        $stmt = $this->connection->prepare($query);
        $stmt->execute();

        return $stmt;
    }
    
    public function update($id, $name, $password)
    {
        $query = 'UPDATE users SET users.name='.$name.' users.password='.$password.' WHERE id='.$id;
        $stmt = $this->connection->prepare($query);
        $stmt->execute();

        return $stmt;
    }
    
    public function delete($id)
    {
        $query = 'DELETE FROM users WHERE id='.$id;
        $stmt = $this->connection->prepare($query);
        $stmt->execute();

        return $stmt;
    }
}