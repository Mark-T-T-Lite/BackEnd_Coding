<html>
<head>
<meta name="viewport"
	content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>Bootstrap Form</title>
<link rel="stylesheet" href="./vendor/bootstrap/css/bootstrap.min.css">
</head>
<body class="bg-light">
	<div class="container">
		<div class="row py-4">
			<div class="col">
				<h2>Bootstrap Form</h2>
			</div>
		</div>
		<form name="frmContact" id="frmContact" method="post" action=""
			enctype="multipart/form-data" novalidate>
			<div class="row">
				<div class="form-group col-md-4">
					<label>Name</label> <span id="userName-info"
						class="invalid-feedback"></span>
					<div class="input-group">
						<div class="input-group-prepend">
							<span class="input-group-text"><?php require __DIR__ . '/vendor/bootstrap/bootstrap-icons/person.svg';?></span>
						</div>
						<input type="text" class="form-control" name="userName"
							id="userName" required>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="form-group col-md-4">
					<label>Email</label> <span id="userEmail-info"
						class="invalid-feedback"></span>
					<div class="input-group">
						<div class="input-group-prepend">
							<span class="input-group-text"><?php require __DIR__ . '/vendor/bootstrap/bootstrap-icons/envelope.svg';?></span>
						</div>
						<input type="email" name="userEmail" id="userEmail"
							class="form-control" required>
					</div>
					<small id="emailHelp" class="form-text text-muted">Your email will
						not be shared.</small>
				</div>
			</div>
			<div class="row">
				<div class="form-group col-md-8">
					<label>Subject</label> <span id="subject-info"
						class="invalid-feedback"></span>
					<div class="input-group">

						<div class="input-group-prepend">
							<span class="input-group-text"><?php require __DIR__ . '/vendor/bootstrap/bootstrap-icons/question.svg';?></span>
						</div>
						<input type="text" name="subject" id="subject"
							class="form-control" required>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="form-group col-md-8">
					<label>Message</label> <span id="content-info"
						class=" invalid-feedback"></span>
					<div class="input-group">
						<div class="input-group-prepend">
							<span class="input-group-text"><?php require __DIR__ . '/vendor/bootstrap/bootstrap-icons/pencil.svg';?></span>
						</div>
						<textarea class="form-control" rows="5" name="message"
							id="message" required></textarea>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="col">
					<input type="submit" name="send" class="btn btn-primary"
						value="Send Message" />
				</div>
			</div>
<?php
if (! empty($displayMessage)) {
    ?>
            <div class="row">
				<div class="col-md-8">
					<div id="statusMessage" class="alert alert-success mt-3"
						role="alert"><?php echo $displayMessage; ?>
					</div>
				</div>
			</div>
<?php
}
?>
		</form>
	</div>
	<script type="text/javascript" src="./js/validation.js"></script>
</body>
</html>