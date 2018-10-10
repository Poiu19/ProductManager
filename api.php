<?php
header('Access-Control-Allow-Origin', '*');
header('Accept: application/json');
header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token');
header('Access-Control-Allow-Credentials: true');

require("dbconfig.php");
if($_SERVER['REQUEST_METHOD'] == 'POST')
{
	$json = file_get_contents('php://input');
	$obj = json_decode($json);
	$config = Array();
	if($obj->getData == 'newsHeaders')
	{
		$sql_query = "	SELECT news.id, news.header, news.content
							FROM news
							ORDER BY news.id DESC";
		$result = mysqli_query($db, $sql_query);
		$config['news'] = Array();
		while($row = mysqli_fetch_assoc($result))
		{
			$config['news'][] = Array('content' => $row['content'], 'header' => $row['header']);  
		}
		mysqli_free_result($result);
		echo json_encode($config['news']);
	}
	if($obj->getData == 'categories')
	{
		$sql_query = " SELECT `id`, `name`, `parent`, `tags` FROM `category` WHERE `id` = `parent`";
		$result = mysqli_query($db, $sql_query);
		$config['category'] = Array();
		while($row = mysqli_fetch_assoc($result))
		{
			$config['category'][] = Array('id' => $row['id'], 'name' => $row['name'], 'parent' => $row['parent'], 'tags' => $row['tags'], 'subcategory' => 0);
		}
		mysqli_free_result($result);
		for($i = 0; $i < count($config['category']); $i++)
		{
			$sql_query = " SELECT `id`, `name`, `parent`, `tags` FROM `category` WHERE `parent` = ". $config['category'][$i]['id'] ." AND `id` != `parent`";
			$result = mysqli_query($db, $sql_query);
			if(mysqli_num_rows($result) != 0)
			{
				$config['category'][$i]['subcategory'] = Array();
				while($row = mysqli_fetch_assoc($result))
				{
					$config['category'][$i]['subcategory'][] = Array('id' => $row['id'], 'name' => $row['name'], 'parent' => $row['parent'], 'tags' => $row['tags'], 'subcategory' => 0);
				}
				mysqli_free_result($result);
			}
			if($config['category'][$i]['subcategory'] != 0)
			{
				for($j = 0; $j < count($config['category'][$i]['subcategory']); $j++)
				{
					$sql_query = " SELECT `id`, `name`, `parent`, `tags` FROM `category` WHERE `parent` = ". $config['category'][$i]['subcategory'][$j]['id'] . " AND `id` != `parent`";
					$result = mysqli_query($db, $sql_query);
					if(mysqli_num_rows($result) != 0)
					{
						$config['category'][$i]['subcategory'][$j]['subcategory'] = Array();
						while($row = mysqli_fetch_assoc($result))
						{
							$config['category'][$i]['subcategory'][$j]['subcategory'][] = Array('id' => $row['id'], 'name' => $row['name'], 'parent' => $row['parent'], 'tags' => $row['tags']);
						}
						mysqli_free_result($result);
					}
				}
			}
		}
		echo json_encode($config['category']);
	}
	if($obj->getData == 'products')
	{
		$sql_query = " SELECT `id`, `name`, `description`, `priceNetto`, `priceBrutto`, `pic`, `new`, `prom` FROM `products` WHERE `category` LIKE '%;". $obj->category .";%';";
		$result = mysqli_query($db, $sql_query);
		$config['products'] = Array();
		while($row = mysqli_fetch_assoc($result))
		{
			$config['products'][] = Array('id' => $row['id'], 'name' => $row['name'], 'description' => $row['description'], 'priceNetto' => $row['priceNetto'], 'priceBrutto' => $row['priceBrutto'], 'pic' => $row['pic'], 'new' => $row['new'], 'prom' => $row['prom']);
		}
		mysqli_free_result($result);
		echo json_encode($config['products']);
	}
	if($obj->getData == 'product')
	{
		$sql_query = "SELECT `products`.`id`, `products`.`name`, `products`.`description_long`, `products`.`priceNetto`, `products`.`priceBrutto`, `products`.`pic`, `products`.`new`, `products`.`prom` FROM `products` WHERE `products`.`id` = ". $obj->productId;
		$result = mysqli_query($db, $sql_query);
		$config['product'] = Array();
		$row = mysqli_fetch_assoc($result);
		$config['product'][] = Array('name' => $row['name'], 'description_long' => $row['description_long'], 'priceNetto' => $row['priceNetto'], 'priceBrutto' => $row['priceBrutto'], 'pic' => $row['pic'], 'new' => $row['new'], 'prom' => $row['prom']);
		echo json_encode($config['product']);
	}
}

?>