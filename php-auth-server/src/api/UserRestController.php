<?php

require_once('../entities/UserDao.php');

class UserRestController
{
    private $connection;

    public function __construct()
    {
        $dc = new DatabaseConnector();
        $this->connection = $dc->getConnection();
    }

    public function index()
    {
        
    }

    
    public function create()
    {
        //
    }

    public function store(Request $request)
    {
        //
    }

    public function show($id)
    {
        $userDao = new UserDao($this->connection);
        return $userDao->read($id);
    }

    public function edit($id)
    {
        //
    }

    public function update(Request $request, $id)
    {
        //
    }

    public function destroy($id)
    {
        //
    }
}